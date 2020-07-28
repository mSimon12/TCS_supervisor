import pandas as pd
import inspect

import OP.EVENTS as events_module


class EventReceiver(object):
    '''
        Class responsible for translating input signals, coming from the real system,
        to responses that are sent to the Product System.

        *To acomplish the translation this class use an auxiliar csv file were the equivalente
        low-level input is associated to an event recognised by the Plant.
            -> At this point is only possible to associate only a single input to each event.
    '''

    def __init__(self):
        # Get all events call in the events_module
        self.__events = {}
        for x in inspect.getmembers(events_module,inspect.isclass):
            self.__events[x[0]] = x[1]  

        # Get translation table (low-level -> high-level)
        filename = "OP/translation_table.csv"
        self.__translation_table = pd.read_csv(filename)

    def receive_event(self, ll_event, param=None):
        '''
            Here you implement the system responsible for receiving input signals.

            As an example, you could run this method as a Thread that monitor the occurance of low-level inputs
            and apply the following code to translate it to high-level event:
        '''
        hl_event = self.__translation_table[(self.__translation_table['low-level']==ll_event)]['high-level'].array        # Translate event

        if hl_event != None:
            self.__events[hl_event[0]].call(param)             # Call execution of the high-level event
