
import os
import errno

import pandas as pd
import numpy as np
from tabulate import tabulate
from graphviz import Digraph
import untangle as ut 

######################################################################################################### 
class MultiAutomata(object):
    '''
        Class for creating multiple automata from a xml file, saving all into a dictionary according their
        names into the file.
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
            a.gen_translation_table()


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
        graph = Digraph(comment=self.__name, filename='{}.gv'.format(self.__name), format='png')
        graph.attr(rankdir='LR')

        if current_state == 'initial':
            current_state = self.__states[self.__states['initial'] == True].index

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
        
        graph.render(f'output/{graph.comment}', view=False)     #Save Automaton as png file


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
        # if not node_name.isupper():
        #     print("Incorrect node name. It must be upper_case!")
        # else:
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

#####----- EVENTS methods: -----###################################################################################
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

        # if event_name.isupper():
        #     print("Incorrect event name. It must be lower_case!")
        # else:
        if event_name not in self.__events:
            self.__events.loc[event_name] = [idt, controllable, 0]          #Add a new event with counter of transitions = 0

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
        filename = "OP/EVENTS.py"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        events_file = open(filename, "a+")                       # Open the file with the events handlers
        events_file.seek(0, os.SEEK_SET)                         # Move the cursor to first line
        content = events_file.read()                             # Read the content of the file

        # Verify if the file is empty
        if os.stat(filename).st_size == 0:
            # Insert importation of pandas
            events_file.write("import pandas as pd\n") 

            # Insert importation of EventDispatcher
            events_file.write("from lib.EventsMonitor import trigger_event\n")    

            # Insert file description
            events_file.write("\n'''")
            events_file.write("\n\tThis file contains all the events (controllable and non-controllable)")
            events_file.write("\n\trelated to the Automata created. Each high-level event has a call method")
            events_file.write("\n\tthat is responsible for executing the event.")
            events_file.write("\n\n\tThe procedures related to each event must be implemented into the 'handler' method.")
            events_file.write("\n\n\t*If desired, the hl_2_ll function can be called into the handler to translate the")
            events_file.write("\n\tcurrent high-level event to a low-level signal configured on the translation_table.csv")
            events_file.write("\n'''")

            # Insert the translation function
            events_file.write("\n\ndef hl_2_ll(hl_event):")
            events_file.write("\n\t'''")
            events_file.write("\n\tThis function is responsible for translating high-level events into low-level signals.")
            events_file.write("\n\t'''")
            events_file.write("\n\t# Get translation table (high-level -> low-level)")
            events_file.write("\n\tfilename = 'OP/translation_table.csv'")
            events_file.write("\n\ttranslation_table = pd.read_csv(filename)")
            events_file.write("\n\tll_event = translation_table[(translation_table['high-level']==hl_event)]['low-level'].array\t# Translate event")
            events_file.write("\n\treturn ll_event\n\n")

        events_file.seek(0, os.SEEK_END)


        #Verify presence of each event and insert if not already defined
        for event in self.__events.index:
            code = "class " + event + "(object):"                                       # Call for event

            if code not in content:
                events_file.write("\n##### -- " + event + " call & handler -- ########################################")
                
                # Event class
                events_file.write("\n" + code)  
                
                # Insert status variable
                events_file.write("\n\t__enabled = {}")
                if self.__events.at[event,'controllable'] == True:
                    events_file.write("\n\t__type = 'controllable'")
                else:
                    events_file.write("\n\t__type = 'uncontrollable'")

                # Insert event call
                events_file.write("\n\n\t@classmethod")
                events_file.write("\n\tdef call(cls, param = None):")
                events_file.write("\n\t\ttrigger_event('" + event + "', " + event + ", param)")

                # Insert event handler
                events_file.write("\n\n\t@classmethod")
                events_file.write("\n\tdef handler(cls, param = None):")
                events_file.write("\n\t\t##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####")
                events_file.write("\n\t\tprint('Executing event "+ event +"...')")
                events_file.write("\n\t\tpass")

                # Insert get status function
                events_file.write("\n\n\t@classmethod")
                events_file.write("\n\tdef get_status(cls):")
                events_file.write("\n\t\t'''\n\t\tTrue: event enabled;\n\t\tFalse: event not allowed.\n\t\t'''")
                events_file.write("\n\t\treturn all(" + event + ".__enabled.values())")

                # Insert get status function
                events_file.write("\n\n\t@classmethod")
                events_file.write("\n\tdef is_controllable(cls):")
                events_file.write("\n\t\treturn " + event + ".__type == 'controllable'")

                #Insert set status function
                events_file.write("\n\n\t@classmethod")
                events_file.write("\n\tdef set_status(cls, name, status):")
                events_file.write("\n\t\t" + event +".__enabled[name] = status\n\n")

        events_file.close()                                             


    def gen_states_calls(self):
        '''
            Generate a file containing calls for the execution of the states 
            present on this Automaton
        '''
        filename = "OP/STATES.py"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        states_file = open(filename, "a+")                                  # Open the file with the states handlers
        states_file.seek(0, os.SEEK_SET)                                    # Move the cursor to first line
        content = states_file.read()                                        # Read the content of the file

        class_name = "class " + self.__name.replace(" ","_") + "(object):"
        if class_name not in content:
            states_file.write("\n" + class_name)

            #Insert states
            for state in self.__states.index:
                code = "def " + state                                       # Call for state

                # if code not in content:
                states_file.write("\n\n\t##### -- " + state.upper() + " handler -- ########################################")

                #State handler
                states_file.write("\n\t@classmethod")
                states_file.write("\n\t" + code + "_handler(self, param = None):")
                states_file.write("\n\t\t#Write code here...")
                # states_file.write("\n\t\tprint('State " + state + " running ...')")
                states_file.write("\n\t\tpass")
            states_file.write("\n\n")
            states_file.close()                                             # Close the access to the file


    def gen_translation_table(self):
        '''
            Generate a csv file with a translation table from high-level to low-level events
        '''
        filename = "OP/translation_table.csv"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        for event in self.__events.index:
            try:
                translation = pd.read_csv(filename)

                if not (event in translation['high-level'].values):
                    translation = pd.DataFrame({'high-level': [event], 'low-level': [np.nan]})
                    translation.to_csv(filename, mode='a', header=False, index=False)
            except:
                translation = pd.DataFrame({'high-level': [event], 'low-level': [np.nan]})
                translation.to_csv(filename, mode='a', header=True, index=False)