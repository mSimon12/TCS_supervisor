
import os
import pandas as pd
from tabulate import tabulate
from graphviz import Digraph
import untangle as ut 


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

    def show_automaton(self):
        '''
            Print a graph representing the supervisor structure
        '''
        graph = Digraph(comment=self.__name, filename='{}.gv'.format(self.__name), format='pdf')

        # Insert nodes in the graph
        for s in self.__states.index:
            graph.node(s,s,shape='circle')

        # insert transitions in the graph
        for t in self.__transitions.index:
            graph.edge(self.__transitions.loc[t,'st_node'],self.__transitions.loc[t,'end_node'],self.__transitions.loc[t,'event'])

        # for s_from in self.__states:
        #     for s_to in self.__states:
        #         transitions = self.__states[s_from].loc[self.__states[s_from]['output_node'] == s_to]
        #         if not transitions.index.empty:
        #             separetor = ','
        #             graph.edge(s_from, s_to, separetor.join(transitions['transition'].values))
        
        graph.view(filename=self.__name,directory='Automaton')      #Save Automaton as pdf file


    def read_xml(self,file):
        '''
            Create the supervisor from a xml file configured as Supremica output
        '''
        aut = ut.parse(file)    #Automaton object
        #Insert states
        for state in aut.Automata.Automaton.States.children:
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
        for event in aut.Automata.Automaton.Events.children:
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
        for trans in aut.Automata.Automaton.Transitions.children:
            source_id = trans['source']
            source = self.__states[self.__states['node_id'] == source_id].index[0]   #Get source name

            dest_id = trans['dest']
            dest = self.__states[self.__states['node_id'] == dest_id].index[0]   #Get destination name

            event_id = trans['event']
            event = self.__events[self.__events['event_id'] == event_id].index[0]   #Get event name

            self.insert_transition(source, dest, event)     #Insert the transition 


    def read_csv(self, file):
        '''
            Create the supervisor from a csv file
        '''
        source_file = pd.read_csv(file)
        pass


    def read_txt(self, file, directory=None):
        '''
            Create the supervisor from a txt file
        '''
        pass

#########################################################################################################    
    #----- GET methods:
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


#########################################################################################################    
    #----- STATES methods:
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

#########################################################################################################
    #----- EVENTS methods:  
    
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


#########################################################################################################    
    #----- TRANSITION methods:
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

#########################################################################################################    
    #----- HANDLERS generation methods:
    def gen_events_calls(self):
        '''
            Generate a file containing calls for the execution of the events 
            present on this Automaton
        '''
        events_file = open("EVENTS.py", "a+")                           # Open the file with the events handlers
        events_file.seek(0, os.SEEK_SET)                         # Move the cursor to first line
        content = events_file.read()                             # Read the content of the file

        if "from threading import Thread" not in content:
            events_file.seek(0, os.SEEK_SET)
            events_file.write("from threading import Thread, Condition\n")                      # Insert importation of Thread
            events_file.seek(0, os.SEEK_END)

        if "from lib.EventMonitor import trigger_event" not in content:
            events_file.seek(0, os.SEEK_SET)
            events_file.write("from lib.EventMonitor import trigger_event\n")         # Insert importation of Event trigger
            events_file.seek(0, os.SEEK_END)

        #Verify presence of each event and insert if not already defined
        for event in self.__events.index:
            code = "class " + event + ":"                                       # Call for event

            if code not in content:
                events_file.write("\n\n\n##### -- " + event + " call & handler -- ########################################")
                
                # Event class
                events_file.write("\n" + code)  
                
                # Insert status variable
                events_file.write("\n\t__count = 0")
                events_file.write("\n\t__enableCond = Condition()")
                events_file.write("\n\t__enabled = {}")

                # Insert event call
                events_file.write("\n\n\tdef call(param = None):")
                events_file.write("\n\t\t" + event + ".__enableCond.acquire()")
                events_file.write("\n\t\t#Verify if all Machines are updated")
                events_file.write("\n\t\twhile " + event + ".__count < len(" + event + ".__enabled):")
                events_file.write("\n\t\t\t" + event + ".__enableCond.wait()")
                events_file.write("\n\t\t" + event + ".__count = 0")

                events_file.write("\n\t\tif all(" + event +".__enabled.values()) == True:")
                events_file.write("\n\t\t\ttrigger_event('" + event + "')")
                events_file.write("\n\t\t\th = Thread(target=" + event + ".__handler, args=[param])")
                events_file.write("\n\t\t\th.start()")
                events_file.write("\n\t\telse:")
                events_file.write("\n\t\t\tprint('" + event + " not enabled!')")
                events_file.write("\n\t\t" + event + ".__enableCond.release()")

                # Insert event handler
                events_file.write("\n\n\tdef __handler(param = None):")
                events_file.write("\n\t\t#Write code here...\n\t\tpass")

                # Insert get status function
                events_file.write("\n\n\tdef get_status():")
                events_file.write("\n\t\t'''\n\t\tTrue: event enabled;\n\t\tFalse: event not allowed.\n\t\t'''")
                events_file.write("\n\t\treturn all(" + event + ".__enabled.values())")

                #Insert set status function
                events_file.write("\n\n\tdef set_status(name, status):")
                events_file.write("\n\t\t" + event + ".__enableCond.acquire()")
                events_file.write("\n\t\t" + event +".__enabled[name] = status")
                events_file.write("\n\t\t" + event + ".__count += 1")
                events_file.write("\n\t\t" + event + ".__enableCond.notify()")
                events_file.write("\n\t\t" + event + ".__enableCond.release()")

        events_file.close()                                             


    def gen_states_calls(self):
        '''
            Generate a file containing calls for the execution of the states 
            present on this Automaton
        '''
        states_file = open("STATES.py", "a+")                                  # Open the file with the states handlers
        states_file.seek(0, os.SEEK_SET)                                # Move the cursor to first line
        content = states_file.read()                                    # Read the content of the file

        if "from threading import Thread" not in content:
            states_file.seek(0, os.SEEK_SET)
            states_file.write("from threading import Thread\n")         # Insert importation of Thread
            states_file.seek(0, os.SEEK_END)

        #Verify presence of each state and insert if not already defined
        for state in self.__states.index:
            code = "def " + state                                       # Call for state

            if code not in content:
                states_file.write("\n\n\n##### -- " + state.upper() + " call & handler -- ########################################")

                # State call
                states_file.write("\n" + code + "(param = None):\n\th = Thread(target=" + state + "_handler, args=[param])\n\th.start()\n")

                #State handler
                states_file.write("\n" + code + "_handler(param = None):\n\tpass\t#Write code here...")
        states_file.close()                                             # Close the access to the file