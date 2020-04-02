
import pandas as pd
from tabulate import tabulate
from graphviz import Digraph

class SupBuilder(object):
    '''
        Class with tools for dinamicaly building an Automaton and displaying it
            sup_name = 'Name for your supervisor automata'
    '''
    def __init__(self, sup_name = 'supervisor'):
        self.__name = sup_name
        self.__states = {}          # Dictionary containing states and transitions directions into a DataFrame
        self.__alphabet = set()     # Alphabet set
        self.__t_count = {}         # Counter of presence of each transition


    def show_supervisor(self):
        '''
            Print a graph representing the supervisor structure
        '''
        graph = Digraph(comment=self.__name, filename='{}.gv'.format(self.__name), format='pdf')

        # Insert nodes in the graph
        for s in self.__states:
            graph.node(s,s,shape='circle')

        # insert transitions in the graph
        for s_from in self.__states:
            for s_to in self.__states:
                transitions = self.__states[s_from].loc[self.__states[s_from]['output_node'] == s_to]
                if not transitions.index.empty:
                    separetor = ','
                    graph.edge(s_from, s_to, separetor.join(transitions['transition'].values))
        
        graph.view(filename=self.__name,directory='Automaton')      #Save Automaton as pdf file
    

    def read_csv(self, file):
        '''
            Create the supervisor from a csv file
        '''
        source_file = pd.read_csv(file)

        for i in source_file.index:
            in_state = source_file.loc[i,source_file.columns[0]]
            t = source_file.loc[i,source_file.columns[1]]
            out_state = source_file.loc[i,source_file.columns[2]]
            #Insert new states
            if not in_state in self.__states:
                self.insert_state(in_state)
            if not out_state in self.__states:
                self.insert_state(out_state)

            #Insert transition
            self.insert_transition(t,in_state,out_state)
    
    def read_txt(self, file, directory=None):
        '''
            Create the supervisor from a txt file
        '''
        pass
    
    
    #----- STATES methods:

    def show_states(self):
        '''
            Show the nodes that belong to the Supervisor.
        '''
       
        for s in self.__states:
            df = self.__states[s]
            pdtabulate= lambda df:tabulate(df,headers='keys')
            print("\nFrom ", s, "to:")
            print(pdtabulate(df))
        print("\nAlphabet = ",self.__alphabet)
        
    
    def insert_state(self, node_name):
        '''
            Insert new node into the Supervisor automaton:
                node_name: UPPER_CASE name
        '''

        if not node_name.isupper():
            print("Incorrect node name. It must be upper_case!")
        else:
            if node_name not in self.__states:
                self.__states[node_name] = pd.DataFrame(columns=['transition', 'output_node'])   #Create a data frame for the new state
            else:
                print("There is already a node called \'",node_name,"\'")


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


    #----- TRANSITION methods:

    def insert_transition(self, t_name, in_node, out_node):
        '''
            Insert a new transition:
                t_name: transistion name;
                in_node: start node of the transition;
                out_node: destiny node from transition.
        '''
        # verify names 
        if t_name.islower() and out_node.isupper():   
            # verify in_node existence      
            if in_node in self.__states:
                # verify existence of the new transition
                if self.__states[in_node].loc[self.__states[in_node]['transition'] == t_name].empty:
                    self.__states[in_node] = self.__states[in_node].append({'transition': t_name , "output_node": out_node}, ignore_index=True)
                    if t_name not in self.__alphabet:
                        self.__t_count[t_name] = 1
                    else:
                        self.__t_count[t_name] += 1
                    self.__alphabet.add(t_name)
                else:
                    print("Transition \'",t_name,"\' already exist from state \'",in_node,"\'")
            else:
                print("Error: Inexistent node!")
        else:
            print("Incorrect names.\n\t Transition --> lower_case!\n\tState --> upper_case!")


    def remove_transition(self, t_name, in_node):
        '''
            Remove a transition from in_node:
        '''
        # verify in_node existence 
        if in_node in self.__states:
            # verify transition existence 
            t_in_node = self.__states[in_node][self.__states[in_node]['transition'] == t_name].index
            if t_name in self.__alphabet and t_in_node != None:
                self.__states[in_node].drop(t_in_node,  inplace=True)  #Remove the desired transition 
                self.__t_count[t_name] -= 1
                if self.__t_count[t_name]==0:
                    self.__alphabet.remove(t_name)      # remove transition from alphabet if not used
            else:
                print("Error: Inexistent transition!")
        else:
            print("Error: Inexistent node!")


#########################################################################################################


class SupMonitor(object):

    def __init__(self, supervisor):
        if not type(supervisor) == SupBuilder:
            print("Error!")
        else:
            self.__supervisor = supervisor
