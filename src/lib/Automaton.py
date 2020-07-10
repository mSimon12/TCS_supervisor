
import os
import errno

import pandas as pd
from tabulate import tabulate
from graphviz import Digraph
import untangle as ut 

######################################################################################################### 
class MultiAutomata(object):
    '''
        Class to generate multiple Automata
    '''
    def __init__(self, block_name):
        self.__name = block_name
        self.__Automata = {}        #Dictionary cantaining all automata by name

    def read_xml(self, file):
        '''
            Read all Automata in the file
        '''
        aut = ut.parse(file)       #Automaton object
        for a in aut.Automata.Automaton:
            G = Automaton(a['name'])
            G.read_xml(file, a['name'])
            self.__Automata[a['name']] = G


    def get_automata(self):
        '''
            Return a dictionary containing all automata by name
        '''
        return self.__Automata


    def generate_calls(self):
        '''
            Create the calls of all events and states present on the set of automata
        '''
        for a in self.__Automata.values():
            a.gen_events_calls()
            a.gen_states_calls()


######################################################################################################### 
class Automaton(object):
    '''
        Class with tools for dinamicaly building an Automaton and displaying it
            aut_name = 'Name for your supervisor automata'
    '''
    def __init__(self, aut_name = 'automaton'):
        self.__name = aut_name
        self.__states = pd.DataFrame(columns=['node_id','initial','accepting'])                 # DataFrame containing states info
        self.__events = pd.DataFrame(columns=['event_id','controllable','transitions'])         # DataFrame containing events info
        self.__transitions = pd.DataFrame(columns=['st_node','end_node','event'])               # DataFrame containing transitions
        self.__alphabet = set()                                                                 # Alphabet set


    def export_automaton(self, current_state = 'initial'):
        '''
            Print a graph representing the supervisor structure
        '''
        graph = Digraph(comment=self.__name, filename='{}.gv'.format(self.__name), format='pdf')
        graph.attr(rankdir='LR')

        if current_state == 'initial':
            current_state = self.__states[self.__states['initial'] == True].index
            print(current_state)

        # Insert nodes in the graph
        n_color = {}

        for s in self.__states.index:
            if self.__states.loc[s,'accepting'] == True:
                n_shape='doublecircle'
            else:
                n_shape = 'circle'

            # if self.__states.loc[s,'initial'] == True:
            if s == current_state:
                n_color['line'] = 'blue'
                n_color['fill'] = 'lightgrey'
            else:
                n_color['line'] = 'black'
                n_color['fill'] = 'white'
                
            graph.node(s,s,shape=n_shape, color= n_color['line'], fillcolor=n_color['fill'], style= 'filled')

        # insert transitions in the graph
        # for t in self.__transitions.index:

        #     if self.__events.loc[self.__transitions.loc[t,'event'],'controllable'] == True:
        #         t_color = 'blue'
        #         t_style = 'filled'
        #     else:
        #         t_color = 'red'
        #         t_style = 'dashed'

        #     graph.edge(self.__transitions.loc[t,'st_node'],self.__transitions.loc[t,'end_node'],self.__transitions.loc[t,'event'], fontcolor = t_color, style = t_style)

        for s_from in self.__states.index:
            for s_to in self.__states.index:
                transitions = self.__transitions[(self.__transitions['st_node'] == s_from) & (self.__transitions['end_node'] == s_to)]
                events = self.__events.loc[transitions['event']]
                cont = events[events['controllable'] == True]
                not_cont = events[events['controllable'] == False]
                if not cont.index.empty:
                    separetor = ',\n'
                    graph.edge(s_from, s_to, separetor.join(cont.index.values), fontcolor='blue')

                if not not_cont.index.empty:
                    separetor = ',\n'
                    graph.edge(s_from, s_to, separetor.join(not_cont.index.values),fontcolor='red', style='dashed')
        
        graph.view(filename=self.__name,directory='output')      #Save Automaton as pdf file


    def read_xml(self, file, auto_name = None):
        '''
            Create the automaton from a xml file configured as Supremica output
            file = the name of the XML file ontaining one or multiple Automata
            aut_name = Name of the desired automaton into a file with multiple Automata  
        '''
        if auto_name == None:
            auto_name = self.__name

        aut_file = ut.parse(file)       #Automaton object

        if len(aut_file.Automata) > 1:
            # Select automaton according name if there is more than one in the xml file
            aut = None
            for x in aut_file.Automata.Automaton:
                if x['name'] == auto_name:
                    aut = x

            if aut == None:
                print("\n >>> Multiple Automata and no Automaton named '" + auto_name + "' on this xml file! <<<\n")
                return False
        else:
            aut = aut_file.Automata.Automaton

        #Insert states
        for state in aut.States.children:
            #Get state id
            idt = state['id']

            #Get initial status
            if state['initial'] == None:
                init = False
            else:
                if state['initial'] == 'false':
                    init = False
                elif state['initial'] == 'true':
                    init = True
            
            #Get accepting status
            if state['accepting'] == None:
                accept = False
            else:
                if state['accepting'] == 'false':
                    accept = False
                elif state['accepting'] == 'true':
                    accept = True

            #Insert the state
            self.insert_state(state['name'], idt, init, accept)

        #Insert events
        for event in aut.Events.children:
            #Get state id
            idt = event['id']

            #Get controllable status
            if event['controllable'] == None:
                cont = True
            else:
                if event['controllable'] == 'false':
                    cont = False
                elif event['controllable'] == 'true':
                    cont = True
            

            #Insert the event
            self.insert_event(event['label'], idt, cont)

        #Insert transitions
        for trans in aut.Transitions.children:
            source_id = trans['source']
            source = self.__states[self.__states['node_id'] == source_id].index[0]   #Get source name

            dest_id = trans['dest']
            dest = self.__states[self.__states['node_id'] == dest_id].index[0]   #Get destination name

            event_id = trans['event']
            event = self.__events[self.__events['event_id'] == event_id].index[0]   #Get event name

            self.insert_transition(source, dest, event)     #Insert the transition 
        
        self.export_automaton()

#####----- GET methods: ------#####################################################################################    
    def get_name(self):
        return self.__name

    def get_alphabet(self):
        return self.__alphabet

    def get_states(self):
        return self.__states

    def get_events(self):
        return self.__events

    def get_transitions(self):
        return self.__transitions

#####----- STATES methods: -----###################################################################################    
    def show_states(self):
        '''
            Show the nodes that belong to the Supervisor.
        '''
       
        pdtabulate= lambda df:tabulate(df,headers='keys')
        print("\nSTATES:")
        print(pdtabulate(self.__states))
        print("\nAlphabet = ",self.__alphabet)
        
    
    def insert_state(self, node_name, idt, initial=False, accepting=True):
        '''
            Insert new node into the Supervisor automaton:
                node_name: UPPER_CASE name
        '''
        if not node_name.isupper():
            print("Incorrect node name. It must be upper_case!")
        else:
            if node_name not in self.__states.index:
                self.__states.loc[node_name] = [idt, initial, accepting]
            else:
                print("There is already a node called \'", node_name,"\'")


    def remove_state(self, node_name):
        '''
            Remove a node from the Supervisor automaton:
        '''
        
        if node_name in self.__states:
            # Discount the counter of each transition starting on this node
            for t in self.__states[node_name]['transition']:
                self.__t_count[t] -= 1
                if self.__t_count[t]==0:
                    self.__alphabet.remove(t)      # Remove transition from alphabet if not used
            
            self.__states.pop(node_name)           # Remove the node
            
            #Remove each transition that ends on this node
            for s in self.__states:
                    t_to_node = self.__states[s][self.__states[s]['output_node']==node_name]['transition'].values              # Transitions to be removed
                    self.__states[s].drop(self.__states[s][self.__states[s]['output_node'] == node_name].index, inplace=True)  # Remove edges to node

                    print(t_to_node)
                    for t in t_to_node:
                        self.__t_count[t] -= 1
                        if self.__t_count[t]==0:
                            self.__alphabet.remove(t)      # Remove transition from alphabet if not used

        elif len(self.__states) == 0:
            print("Error: Empty supervisor!")
        else:
            print("Error: Inexistent node!")

#### #----- EVENTS methods: -----###################################################################################
    def show_events(self):
        '''
            Show the events that belong to the Supervisor.
        '''
        pdtabulate= lambda df:tabulate(df,headers='keys')
        print("\nEVENTS:")
        print(pdtabulate(self.__events))
        print("\nAlphabet = ",self.__alphabet)


    def insert_event(self, event_name, idt, controllable=True):
        '''
            Insert new event type into the Automaton:
                event_name: LOWER_CASE name
        '''

        if event_name.isupper():
            print("Incorrect event name. It must be lower_case!")
        else:
            if event_name not in self.__events:
                self.__events.loc[event_name] = [idt, controllable, 0]              #Add a new event with counter of transitions = 0

                self.__alphabet.add(event_name)                                 #Add the new event to the alphabet
            else:
                print("There is already a event called \'",event_name,"\'")


    def remove_event(self, event_name):
        '''
            Remove a specific event:
        '''
        pass

######----- TRANSITION methods: ------##############################################################################    
    def show_transitions(self):
        '''
            Show the nodes that belong to the Supervisor.
        '''
       
        pdtabulate= lambda df:tabulate(df,headers='keys')
        print("\nTRANSITIONS:")
        print(pdtabulate(self.__transitions))
        print("\nAlphabet = ",self.__alphabet)


    def insert_transition(self, st_node, end_node, event):
        '''
            Insert a new transition:
                st_node: start node of the transition;
                end_node: destiny node from transition;
                event: event that trigger the transition.
        '''
        # Verifye event existance
        if event in self.__events.index:
            # Verifye states existance
            if st_node in self.__states.index and end_node in self.__states.index:
                # Verifye transition existance
                if self.__transitions[(self.__transitions['st_node'] == st_node) & (self.__transitions['event'] == event)].empty:
                    self.__transitions = self.__transitions.append({'st_node':st_node, 'end_node':end_node, 'event':event}, ignore_index=True)
                    self.__events.loc[event,'transitions'] += 1
                else:
                    print("Transition already exist!")
            else:
                print("Some state have not been created!")
        else:
            print("Event ", event, "does not exist!")


    def remove_transition(self, st_node, event):
        '''
            Remove a transition from in_node:
        '''
        # verify in_node existence 
        if st_node in self.__states.index:
            # verify transition existence 
            if self.__transitions[(self.__transitions['st_node'] == st_node) & (self.__transitions['event'] == event)].empty:
                print("There is no transition with ",event,"leaving the state ",st_node,"!.")
            else:
                self.__transitions.drop(self.__transitions[self.__transitions['st_node'] == st_node][self.__transitions['event'] == event].index,inplace=True)
                self.__events.loc[event,'transitions'] -= 1
        else:
            print("Error: Inexistent node!")

#####----- HANDLERS generation methods: ------######################################################################    
    def gen_events_calls(self):
        '''
            Generate a file containing calls for the execution of the events 
            present on this Automaton
        '''
        filename = "handlers/EVENTS.py"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        events_file = open(filename, "a+")                           # Open the file with the events handlers
        events_file.seek(0, os.SEEK_SET)                         # Move the cursor to first line
        content = events_file.read()                             # Read the content of the file

        # Insert importation of Thread
        if "from threading import Thread" not in content:
            events_file.seek(0, os.SEEK_SET)
            events_file.write("from threading import Thread, Condition\n")                      
        
        # Insert global variables and mutexes
        if "class g_var:" not in content:
            events_file.write("\n# Global variables and mutexes")
            events_file.write("\nclass g_var:")
            events_file.write("\n\tSM_status = {}")
            events_file.write("\n\tSM_mutex = Condition()")
            events_file.write("\n\tlast_event = None")
            events_file.write("\n\treq_SM_update = Condition()") 

        # Insert general event caller
        if "def trigger_event" not in content:
            events_file.write("\n\n##### -- General event caller -- ########################################")
            events_file.write("\ndef trigger_event(event, handler, param):")
            events_file.write("\n\t'''\n\t\tTrigger event handler and notify State Machines about the event occured.\n\t'''")
            
            events_file.write("\n\tg_var.SM_mutex.acquire()")
            events_file.write("\n\t#Verify if all Machines are updated")
            events_file.write("\n\twhile (not all(g_var.SM_status.values()) or (not bool(g_var.SM_status))):")
            events_file.write("\n\t\tg_var.SM_mutex.wait()\n")

            events_file.write("\n\t#Verify if all SM enable this event")	
            events_file.write("\n\tg_var.req_SM_update.acquire()")
            events_file.write("\n\tif eval(event).get_status() == True:")
            events_file.write("\n\t\tg_var.SM_status = {x: False for x in g_var.SM_status}	# Clear all SM status")
            events_file.write("\n\t\tg_var.last_event = event")  
            events_file.write("\n\t\th = Thread(target=handler, args=[param])")
            events_file.write("\n\t\th.start()")
            events_file.write("\n\t\th.join()")
            events_file.write("\n\n\t\t# Notify State Machines the need of update")
            events_file.write("\n\t\ttry:")
            events_file.write("\n\t\t\tg_var.req_SM_update.notifyAll()")
            events_file.write("\n\t\texcept RuntimeError:")
            events_file.write("\n\t\t\tprint('ERROR: Unable to notify new event!')")
            events_file.write("\n\telse:")
            events_file.write("\n\t\tprint(event, ' not enabled!')")
            events_file.write("\n\tg_var.req_SM_update.release()")
            events_file.write("\n\tg_var.SM_mutex.release()")
          
        events_file.seek(0, os.SEEK_END)

        #Verify presence of each event and insert if not already defined
        for event in self.__events.index:
            code = "class " + event + ":"                                       # Call for event

            if code not in content:
                events_file.write("\n\n\n##### -- " + event + " call & handler -- ########################################")
                
                # Event class
                events_file.write("\n" + code)  
                
                # Insert status variable
                events_file.write("\n\t__enabled = {}")

                # Insert event call
                events_file.write("\n\n\tdef call(param = None):")
                events_file.write("\n\t\ttrigger_event('" + event + "', " + event + ".__handler, param)")

                # Insert event handler
                events_file.write("\n\n\tdef __handler(param = None):")
                events_file.write("\n\t\t#Write code here...")
                events_file.write("\n\t\tprint('Executing event "+ event +"...')")
                events_file.write("\n\t\tpass")

                # Insert get status function
                events_file.write("\n\n\tdef get_status():")
                events_file.write("\n\t\t'''\n\t\tTrue: event enabled;\n\t\tFalse: event not allowed.\n\t\t'''")
                events_file.write("\n\t\treturn all(" + event + ".__enabled.values())")

                #Insert set status function
                events_file.write("\n\n\tdef set_status(name, status):")
                events_file.write("\n\t\t" + event +".__enabled[name] = status")

        events_file.close()                                             


    def gen_states_calls(self):
        '''
            Generate a file containing calls for the execution of the states 
            present on this Automaton
        '''
        filename = "handlers/STATES.py"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        states_file = open(filename, "a+")                                  # Open the file with the states handlers
        states_file.seek(0, os.SEEK_SET)                                # Move the cursor to first line
        content = states_file.read()                                    # Read the content of the file

        if "from handlers.EVENTS import" not in content:
            states_file.seek(0, os.SEEK_SET)
            states_file.write("from handlers.EVENTS import *\n")         # Insert importation of Thread
        
        states_file.seek(0, os.SEEK_END)

        class_name = "class " + self.__name.replace(" ","_") + ":"
        if class_name not in content:
            states_file.write("\n\n" + class_name)

            #Insert states
            for state in self.__states.index:
                code = "def " + state                                       # Call for state

                # if code not in content:
                states_file.write("\n\n\t##### -- " + state.upper() + " handler -- ########################################")

                #State handler
                states_file.write("\n\t" + code + "_handler(param = None):")
                states_file.write("\n\t\t#Write code here...")
                states_file.write("\n\t\tprint('State " + state + " running ...')")
                states_file.write("\n\t\tpass")
            states_file.close()                                             # Close the access to the file