
import inspect
import pandas as pd
from threading import Thread
from multiprocessing import Process

from lib.Automaton import Automaton
from lib.ProductSystem import g_var

import OP.EVENTS as events_module
# from OP.STATES import *                     # Implemented only for state-based approach

######################################################################################################### 
class StateMachine(Thread):
    '''
        Class for the execution of a State Machine as a thread.
    '''
    def __init__(self, automaton):
        Thread.__init__(self)                                                                   # Initialize the thread
        self.__name = automaton.get_name().replace(" ","_")                                     # Name of the StateMachine
        self.__SM = automaton                                                                   # Use the automaton as SM

        # Get all events call in the module
        self.__events_list = {}
        for x in inspect.getmembers(events_module,inspect.isclass):                             # Get events classes in a dictionary
            self.__events_list[x[0]] = x[1] 

    def run(self):
        states = self.__SM.get_states()                                                         # Get the states of the Automaton
        events = self.__SM.get_events()                                                         # Get the events of the Supervisor
        alpha = self.__SM.get_alphabet()                                                        # Get the alphabet of the Automaton
        trans = self.__SM.get_transitions()                                                     # Get the transitions of the Automaton
        current_state = states.loc[states['initial'] == True].index[0]                          # Get initial state

        ###### For state-based approaches ####################################################
        # # Call execution of the initial node
        # s = Process(target=eval(self.__name + "." + current_state + "_handler"), args=[None])
        # s.start()
        # last_s = s
        ######################################################################################

        # Loop to control the State Machine
        while True:
            # Enable and disable events
            for e in alpha:
                if (not trans[(trans['st_node'] == current_state) & (trans['event'] == e)].empty) or (events.loc[e,'controllable'] == False):
                    # Enable event
                    self.__events_list[e].set_status(self.__name, True)
                else:
                    # Disable event
                    self.__events_list[e].set_status(self.__name, False)

            # Inform event monitor that the SM is updated
            g_var.SM_update_flag.acquire()
            g_var.SM_status[self.__name] = True                 # Signal that the status have been updated
            g_var.SM_update_flag.notify()                       # Notify EventsMonitor that this State Machine is updated
            
            g_var.new_event.acquire()                           # Acquire access to the event section
            g_var.SM_update_flag.release()                      # Release the mutex for SM status
            
            try:
                g_var.new_event.wait()                          # Wait the occurence of a new event
            except RuntimeError:
                print("[SM - " + self.__name + "]: ERROR: Unable to wait new event!")
            
            event = g_var.last_event                            # Get the last occured event
            g_var.new_event.release()                           # Release access to the event section

            # Verify if the event belongs to this State Machine
            if event in alpha:
                # Verify if the event trigger a transition
                if trans[(trans['st_node'] == current_state) & (trans['event'] == event)].empty:
                    print("[SM - " + self.__name + "]: ALERT!!!!\tThis transition is not modeled!")
                else:
                    current_state = trans.at[trans[(trans['st_node'] == current_state) & (trans['event'] == event)].index[0],'end_node']
                    # print("[SM - " + self.__name + "]: New state:  ", current_state)

                    ###### For state-based approaches ####################################################
                    # # Terminate the execution of the last node
                    # last_s.terminate()
                    # last_s.join()
                    
                    # # Call execution of the current node
                    # s = Process(target=eval(self.__name + "." + current_state + "_handler"), args=[None])
                    # s.start()
                    # last_s = s
                    ######################################################################################

                    # Print the automaton
                    self.__SM.export_automaton(current_state)
                    
            else:
                # print("The event '",event,"' does not exist on this SM!")
                pass
                                

######################################################################################################### 
class Supervisor(Thread):
    '''
        Class to run a Supervisor for dinamically monitor the system and disable/enable controllable events
    '''
    def __init__(self, automaton):
        Thread.__init__(self)                                                                   # Initialize the thread
        self.__name = automaton.get_name().replace(" ","_")                                     # Name of the StateMachine
        self.__SUP = automaton                                                                  # Use the automaton as SUP

        # Get all events call in the module
        self.__events_list = {}                                                                 
        for x in inspect.getmembers(events_module,inspect.isclass):                             # Get events classes in a dictionary
            self.__events_list[x[0]] = x[1] 

    def run(self):
        states = self.__SUP.get_states()                                                         # Get the states of the Supervisor
        events = self.__SUP.get_events()                                                         # Get the events of the Supervisor
        alpha = self.__SUP.get_alphabet()                                                        # Get the alphabet of the Supervisor
        trans = self.__SUP.get_transitions()                                                     # Get the transitions of the Supervisor
        current_state = states.loc[states['initial'] == True].index[0]                           # Get initial state

        # Loop to control the Supervisor current state
        while True:
            # Enable and disable events
            for e in alpha:
                if (not trans[(trans['st_node'] == current_state) & (trans['event'] == e)].empty) or (events.loc[e,'controllable'] == False):
                    # Enable event
                    self.__events_list[e].set_status(self.__name, True)
                else:
                    # Disable event
                    self.__events_list[e].set_status(self.__name, False)

            # Inform event monitor that the SM is updated
            g_var.SM_update_flag.acquire()
            g_var.SM_status[self.__name] = True                 # Signal that the status have been updated
            g_var.SM_update_flag.notify()                       # Notify EventsMonitor that this Supervisor is updated
            
            g_var.new_event.acquire()                           # Acquire access to the event section
            g_var.SM_update_flag.release()                      # Release the mutex for SM status
             
            try:
                g_var.new_event.wait()                          # Wait the occurence of a new event
            except RuntimeError:
                print("[SUP - " + self.__name + "]: ERROR: Unable to wait new event!")
              
            event = g_var.last_event                            # Get the last occured event
            g_var.new_event.release()                           # Release access to the event section

            # Verify if the event belongs to this State Machine
            if event in alpha:
                # Verify if the event trigger a transition
                if trans[(trans['st_node'] == current_state) & (trans['event'] == event)].empty:
                    print("[SUP - " + self.__name + "]: ALERT!!!!\tThis transition is not modeled!")
                else:
                    current_state = trans.at[trans[(trans['st_node'] == current_state) & (trans['event'] == event)].index[0],'end_node']
                    # print("[SUP - " + self.__name + "]: New state:  ", current_state)

                # Print the automaton
                self.__SUP.export_automaton(current_state)
            else:
                # print("The event '",event,"' does not exist on this SUP!")
                pass