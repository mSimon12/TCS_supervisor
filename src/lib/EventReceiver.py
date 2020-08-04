import pandas as pd
import inspect

from lib.ProductSystem import trigger_event

class EventReceiver(object):
    '''
        Class responsible for translating input signals, coming from the real system,
        to responses that are sent to the Product System.

        *To acomplish the translation this class use an auxiliar csv file were the equivalente
        low-level input is associated to an event recognised by the Plant.
            -> At this point is only possible to associate only a single input to each event.
    '''

    def __init__(self):
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
            trigger_event(hl_event[0], param)                  # Trigger the received event