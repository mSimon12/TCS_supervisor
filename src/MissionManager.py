import time
import inspect

from threading import Thread, Condition
import OP.EVENTS as events_module
from lib.EventDispatcher import g_var

from OP.EVENTS import *

class MissionManager(Thread):
    '''
        This class implements the Mission Manager, component responsible for deciding wich 
        enabled event to be triggered in the next step.

        This is a Thread, so you can implement a loop into the 'run' method that constantly
        updates the event to be executed.
    '''

    def __init__(self):
        Thread.__init__(self)   

    def get_last_event(self):
        g_var.req_SM_update.acquire()
        last = g_var.last_event
        g_var.req_SM_update.release()

        return last

    
    def run(self):
        # Get all events call in the events_module
        events = {}
        for x in inspect.getmembers(events_module,inspect.isclass):
            events[x[0]] = x[1]  

        # On this exemple the Mission Manager will anly run the following events
        events_to_execute = ['on_gs', 'on_vs', 'st_app', 'end_app', 'off_vs', 'off_gs']

        for e in events_to_execute:
            print("\nLast event --> ", self.get_last_event())
            events[e].call()
           