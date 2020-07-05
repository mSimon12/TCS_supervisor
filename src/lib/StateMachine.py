import pandas as pd
from threading import Thread

from lib.Automaton import Automaton
from handlers.EVENTS import *
from handlers.STATES import *

######################################################################################################### 
class StateMachine(Thread):
    '''
        Class with tools for dinamicaly building an Automaton and displaying it
            aut_name = 'Name for your supervisor automata'
    '''
    def __init__(self, automaton):
        Thread.__init__(self)                                                                   # Initialize the thread
        self.__name = automaton.get_name().replace(" ","_")                                     # Name of the StateMachine
        self.__SM = automaton                                                                   # Use the automaton as SM

    def run(self):
        states = self.__SM.get_states()                                                         # Get the states of the Automaton
        alpha = self.__SM.get_alphabet()                                                        # Get the events of the Automaton
        trans = self.__SM.get_transitions()                                                     # Get the alphabet of the Automaton
        current_state = states.loc[states['initial'] == True].index[0]                          # Get initial state

        # Call execution of the current node
        eval(self.__name + "." + current_state)()

        # Loop to control the State Machine
        while True:
            # Enable and disable events
            for e in alpha:
                if trans[(trans['st_node'] == current_state) & (trans['event'] == e)].empty:
                    # Disable event
                    eval(e).set_status(self.__name, False)
                else:
                    # Enable event
                    eval(e).set_status(self.__name, True)

            # Inform event monitor that the SM is updated
            g_var.SM_mutex.acquire()
            g_var.SM_status[self.__name] = True
            g_var.SM_mutex.notify()

            # Acquire access to the event section
            g_var.req_SM_update.acquire()   

            # Release the mutex for SM status                        
            g_var.SM_mutex.release()
            
            try:
                g_var.req_SM_update.wait()                          # Wait the occurence of a new event
            except RuntimeError:
                print("ERROR: Unable to wait new event!")
            
            event = g_var.last_event                                # Get the last occured event

            # Verify if the event belongs to this State Machine
            if event in alpha:
                # Verify if the event trigger a transition
                if trans[(trans['st_node'] == current_state) & (trans['event'] == event)].empty:
                    print("ALERT!!!!\nThis transition should not have occured!")
                else:
                    current_state = trans.at[trans[(trans['st_node'] == current_state) & (trans['event'] == event)].index[0],'end_node']
                    print("\nNew state:  ", current_state)
                    # Call execution of the current node
                    eval(self.__name + "." + current_state)()
            else:
                print("The event '",event,"' does not exist on this SM!")
            
            # Release access to the event section
            g_var.req_SM_update.release()                       