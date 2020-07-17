
import pandas as pd
import inspect

import handlers.EVENTS as events_module

class EventReceiver(object):

    def __init__(self):
        # Get all events call in the module
        self.__events = {}
        for x in inspect.getmembers(events_module,inspect.isclass):
            self.__events[x[0]] = x[1]  

        # Get translation table (low-level -> high-level)
        filename = "handlers/translation_table.csv"
        self.__transistions_table = pd.read_csv(filename)

    def receive_event(msg):
        pass
