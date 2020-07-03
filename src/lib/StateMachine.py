import pandas as pd
from threading import Thread

from lib.Automaton import Automaton
import lib.EventMonitor as em
from EVENTS import *

######################################################################################################### 
class StateMachine(Thread):
    '''
        Class with tools for dinamicaly building an Automaton and displaying it
            aut_name = 'Name for your supervisor automata'
    '''
    def __init__(self, automaton):
        Thread.__init__(self)                                                                   #  Initialize the thread
        self.__name = automaton.get_name()                                                      # Name of the StateMachine
        self.__SM = automaton                                                                   # Use the automaton as SM

    def run(self):
        # global last_event, event_occured

        states = self.__SM.get_states()                                                         # Get the states of the Automaton
        alpha = self.__SM.get_alphabet()                                                        # Get the events of the Automaton
        trans = self.__SM.get_transitions()                                                     # Get the alphabet of the Automaton
        current_state = states.loc[states['initial'] == True].index[0]                          # Get initial state

        # Enable and disable events
        for e in alpha:
            if trans[(trans['st_node'] == current_state) & (trans['event'] == e)].empty:
                # Disable event
                eval(e).set_status(self.__name, False)
            else:
                # Enable event
                eval(e).set_status(self.__name, True)

        last_received_event = None
        # Initialize Loop to control the State Machine
        while True:
            em.event_occured.acquire()                           # Acquire access to the event section
            while last_received_event == em.last_event:
                try:
                    em.event_occured.wait()                      # Wait the occurence of a new event
                except RuntimeError:
                    print("ERROR: Unable to wait new event!")
                em.event_occured.release()                       # Release access to the event section
            event = em.last_event                                # Get the last occured event
            last_received_event = event
            print("2 - state update")

            # Verify if the event belongs to this State Machine
            if event in alpha:
                # Verify if the event trigger a transition
                if trans[(trans['st_node'] == current_state) & (trans['event'] == event)].empty:
                    print("ALERT!!!!\nThis transition should not have occured!")
                else:
                    current_state = trans.at[trans[(trans['st_node'] == current_state) & (trans['event'] == event)].index[0],'end_node']
                    print("New state:  ", current_state)

                    # Enable and disable events
                    for e in alpha:
                        if trans[(trans['st_node'] == current_state) & (trans['event'] == e)].empty:
                            # Disable event
                            eval(e).set_status(self.__name, False)
                        else:
                            # Enable event
                            eval(e).set_status(self.__name, True)

            else:
                print("The event '",event,"' does not exist on this SM!")

