import inspect
import pandas as pd

from lib.Automaton import Automaton

import OP.EVENTS as events_module
         
######################################################################################################### 
class StateMachine(object):
    '''
        Class for the execution of a State Machine.
        - The method update executes:
            1- Verify if the event belongs to this Plant and update the states if needed;
            2- Updates list of controllable events allowed by this Plant
        
        * Uncontrollable events are always allowed.
    '''
    def __init__(self, automaton):
        '''
            The execution of the State Machines depends on the attribution of an Automaton to be executed.
                automaton: object of Class Automaton.
        '''
        self.__SM = automaton
        self.__name = automaton.get_name().replace(" ","_")                                     # Name of the StateMachine
        self.__states = automaton.get_states()                                                  # Get the states of the Automaton
        self.__events = automaton.get_events()                                                  # Get the events of the Automaton
        self.__alpha = automaton.get_alphabet()                                                 # Get the alphabet of the Automaton
        self.__trans = automaton.get_transitions()                                              # Get the transitions of the Automaton
        self.__current_state = self.__states.loc[self.__states['initial'] == True].index[0]     # Get initial state

        # Get all events call in the module
        self.__events_list = {}
        for x in inspect.getmembers(events_module,inspect.isclass):                             # Get events classes in a dictionary
            self.__events_list[x[0]] = x[1] 

        # Enable and disable events
        for e in self.__alpha:
            if (not self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == e)].empty) or (self.__events.loc[e,'controllable'] == False):
                self.__events_list[e].set_status(self.__name, True)         # Enable event
            else:
                self.__events_list[e].set_status(self.__name, False)        # Disable event


    def get_state(self):
        '''
            Get the current state of this State Machine
        '''
        return self.__current_state
    

    def state_update(self, event):
        '''
            Update the state of this state machine after occurance of the specified event
            and update the enabled events.
        '''
        # Verify if the event belongs to this State Machine
        if event in self.__alpha:
            # Verify if the event trigger a transition
            if self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == event)].empty:
                print("[SM - " + self.__name + "]: ALERT!!!!\tThis transition is not modeled!")         # Alert if the last event was not modeled by this plant, but on its alphabet
            else:
                # Update current state
                self.__current_state = self.__trans.at[self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == event)].index[0],'end_node']
                # print("[SM - " + self.__name + "]: New state:  ", self.__current_state)

                # Export the automaton
                self.__SM.export_automaton(self.__current_state)      

            # Enable and disable events that belong to this SM
            for e in self.__alpha:
                if (not self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == e)].empty) or (self.__events.loc[e,'controllable'] == False):
                    self.__events_list[e].set_status(self.__name, True)         # Enable event
                else:
                    self.__events_list[e].set_status(self.__name, False)        # Disable event
        else:
            # print("The event '",event,"' does not exist on this SM!")
            pass

        
######################################################################################################### 
class Supervisor(object):
    '''
        Class for the execution of a Supervisor.
        - The method update executes:
            1- Verify if the event belongs to this Supervisor and update the states if needed;
            2- Updates list of controllable events allowed by this Supervisor
        
        * Uncontrollable events are always allowed.
    '''

    def __init__(self, automaton):
        '''
            The execution of the Supervisor depends on the attribution of an Automaton to be executed.
                automaton: object of Class Automaton.
        '''
        self.__SUP = automaton
        self.__name = automaton.get_name().replace(" ","_")                                     # Name of the Supervisor
        self.__states = automaton.get_states()                                                  # Get the states of the Automaton
        self.__events = automaton.get_events()                                                  # Get the events of the Automaton
        self.__alpha = automaton.get_alphabet()                                                 # Get the alphabet of the Automaton
        self.__trans = automaton.get_transitions()                                              # Get the transitions of the Automaton
        self.__current_state = self.__states.loc[self.__states['initial'] == True].index[0]     # Get initial state

        # Get all events call in the module
        self.__events_list = {}
        for x in inspect.getmembers(events_module,inspect.isclass):                             # Get events classes in a dictionary
            self.__events_list[x[0]] = x[1] 

        # Enable and disable events
        for e in self.__alpha:
            if (not self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == e)].empty) or (self.__events.loc[e,'controllable'] == False):
                self.__events_list[e].set_status(self.__name, True)         # Enable event
            else:
                self.__events_list[e].set_status(self.__name, False)        # Disable event


    def get_state(self):
        '''
            Get the current state of this Supervisor
        '''
        return self.__current_state
    
    
    def state_update(self, event):
        '''
            Update the state of this Supervisor after occurance of the specified event
            and update the enabled events.
        '''
        # Verify if the event belongs to this Supervisor
        if event in self.__alpha:
            # Verify if the event trigger a transition
            if self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == event)].empty:
                print("[SUP - " + self.__name + "]: ALERT!!!!\tThis transition is not modeled!")         # Alert if the last event was not modeled by this plant, but on its alphabet
            else:
                # Update current state
                self.__current_state = self.__trans.at[self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == event)].index[0],'end_node']
                # print("[SUP - " + self.__name + "]: New state:  ", self.__current_state)

                # Export the automaton
                self.__SUP.export_automaton(self.__current_state)      

            # Enable and disable events that belong to this SUP
            for e in self.__alpha:
                if (not self.__trans[(self.__trans['st_node'] == self.__current_state) & (self.__trans['event'] == e)].empty) or (self.__events.loc[e,'controllable'] == False):
                    self.__events_list[e].set_status(self.__name, True)         # Enable event
                else:
                    self.__events_list[e].set_status(self.__name, False)        # Disable event
        else:
            # print("The event '",event,"' does not exist on this SUP!")
            pass