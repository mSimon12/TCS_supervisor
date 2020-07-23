import time
import inspect
import pandas as pd
from threading import Thread, Condition

from lib.ProductSystem import g_var
import OP.EVENTS as events_module

class MissionManager(Thread):
    '''
        This class implements the Mission Manager, component responsible for deciding wich 
        enabled event to be triggered in the next step.

        This is a Thread, so you can implement a loop into the 'run' method that constantly
        updates the event to be executed.
    '''

    def __init__(self):
        Thread.__init__(self)   

        # Get all events call in the module
        self.__cont_events = {}
        for x in inspect.getmembers(events_module,inspect.isclass):
            if x[1].is_controllable():
                self.__cont_events[x[0]] = x[1]  

    def get_last_update(self):
        g_var.trace_update_flag.acquire()
        while g_var.events_trace.empty:
            g_var.trace_update_flag.wait()
        current_status = g_var.events_trace.tail(1)        # Get the last update
        g_var.trace_update_flag.release()

        return current_status

    
    def run(self):
        # On this exemple the Mission Manager will only run the following events
        events_to_execute = ['on_gs', 'st_app', 'on_vs', 'st_app', 'off_vs', 'off_gs']

        for e in events_to_execute:
            # Get last update in Machines
            current = self.get_last_update()
            if current.index[0] > 0:
                last_event = current['event'].array[0]
                print("\nLast event --> ", last_event)

            # Print enabled events
            enabled_events = current['enabled_events'].array[0]
            print("Enabled_events --> ", enabled_events)

            # Print current states
            print("Current states: ")
            for s in current['states'].values[0]:
                print(f"\t{s.upper()}: {current['states'].values[0][s]}")
            print()

            if e in enabled_events:
                self.__cont_events[e].call()
            else: 
                print(f"\nEvent '{e}' is not enabled!")
            time.sleep(2)
           