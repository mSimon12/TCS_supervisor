import time
import inspect
import pandas as pd
from threading import Thread, Condition

from lib.ProductSystem import g_var, trigger_event
# import OP.EVENTS as events_module

class MissionManager(Thread):
    '''
        This class implements the Mission Manager, component responsible for deciding wich 
        enabled event to be triggered in the next step.

        This is a Thread, so you can implement a loop into the 'run' method that constantly
        updates the event to be executed.
    '''

    def __init__(self):
        Thread.__init__(self)   

        self.__last_id = -1                                             # Variable to control new events received

        # Get all events call in the module
        # self.__cont_events = {}
        # for x in inspect.getmembers(events_module,inspect.isclass):
        #     if x[1].is_controllable():
        #         self.__cont_events[x[0]] = x[1]  

    def get_last_update(self):
        g_var.trace_update_flag.acquire()
        while (g_var.events_trace.empty) or (self.__last_id == g_var.events_trace.tail(1).index[0]):
            print("[Mission Manager]: Waiting next update!")
            g_var.trace_update_flag.wait()
        current_status = g_var.events_trace.tail(1)         # Get the last update
        self.__last_id = current_status.index[0]            # Get id of the last occured event
        g_var.trace_update_flag.release()

        return current_status


    def wait_events(self, time = 0.5):
        '''
            Wait till the moment when there is no event for 'time' seconds.
        '''
        timeout = False
        while not timeout:
            g_var.trace_update_flag.acquire()
            timeout = not g_var.trace_update_flag.wait(time)
            g_var.trace_update_flag.release()
    
    def run(self):
        # On this exemple the Mission Manager will only run the following events
        events_to_execute = ['on_gs', 'on_vs', 'st_app', 'off_vs', 'off_gs']

        for e in events_to_execute:
            self.wait_events()                                                  # Wait till all triggered events have occured
            
            # Get last update in Machines
            current = self.get_last_update()
            if current.index[0] > 0:
                last_event = current['event'].array[0]
                print("\n[Mission Manager]: Last event --> {} (param = {})".format(last_event, current['event_params']))

            # Print enabled events
            enabled_events = current['enabled_events'].array[0]
            print("[Mission Manager]: Enabled_events --> ", enabled_events)

            # Print current states
            print("[Mission Manager]: Current states: ")
            for s in current['states'].values[0]:
                print(f"\t{s.upper()}: {current['states'].values[0][s]}")
            print()

            if e in enabled_events:
                trigger_event(e)                                                    # Call the execution of the controllable event
                print("MM calling!")
            else: 
                print(f"\n[Mission Manager]: Event '{e}' is not enabled!")
            time.sleep(2)
           