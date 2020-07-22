from threading import Thread
import PySimpleGUI as sg
import inspect
import os
import pandas as pd

from lib.EventReceiver import EventReceiver
from lib.ProductSystem import g_var

import OP.EVENTS as events_module
import OP.STATES as states_module

class EventInterface(Thread):
    '''
        Interface for executing events and visualizing automata.
    '''

    def __init__(self):
        Thread.__init__(self)  

        # Set environment variable required for the Interface execution
        os.environ["DISPLAY"]=":0"

        self.current_status_id = -1

        # Get name of the Machines
        machines = [s[0] for s in inspect.getmembers(states_module,inspect.isclass)]

        # Get all events call in the module
        self.__events = {}
        for x in inspect.getmembers(events_module,inspect.isclass):
            self.__events[x[0]] = x[1]  

        # Get controllable events
        self.__cont_e = [e for e in self.__events if self.__events[e].is_controllable()]
       
        # Get uncontrollable events
        self.__not_cont_e = [e for e in self.__events if not self.__events[e].is_controllable()]

        # Get translation table
        filename = "OP/translation_table.csv"
        translation_table = pd.read_csv(filename)
        
        # Translate non-controllable events to low-level call
        self.__not_cont_inputs = []
        for hl_event in self.__not_cont_e:
            self.__not_cont_inputs.append(translation_table[(translation_table['high-level']==hl_event)]['low-level'].array[0])

        # Object to simulate non-controllable events
        self.__receiver = EventReceiver()

        #####################################################################################################################
        #Layout
        layout =[ 
            [sg.Text('Current machine:'), sg.InputCombo(values=machines, default_value=machines[0], size=(35,10), key='option', enable_events=True)],
            [sg.Image("output/" + machines[0] + ".png", key="_IMAGE_", background_color="white")],
            [sg.Text('Trigger event')],
            [sg.Radio('Controllable','event_type', default=False, key='controllable',enable_events=True), sg.Radio('Uncontrollable','event_type', default=True, key='uncontrollable',enable_events=True)],
            [sg.InputCombo(values = self.__not_cont_inputs, default_value= self.__not_cont_inputs[0], size=(20,10), key='selected_event', enable_events=True), sg.Button('TRIGGER', key='trigger')]
        ]

        #Janela
        self.janela = sg.Window("State Machine visualizer", size=(1000,500)).layout(layout)
        
        
    def run(self):
        self.event_type = 'uncontrollable'
        self.enabled_e = []
        trace = Thread(target=self.events_trace)
        trace.start()                                                       # Start event tracer as a thread

        while True:
            #Extrair os dados da tela
            event, values = self.janela.Read(timeout=1000)
            if event in (None, 'Cancel'):   # if user closes window or clicks cancel
                print('\nCLOSING EVENT INTERFACE ...\n')
                break

            #Update the Automaton Image
            try:
                self.janela.Element("_IMAGE_").update(filename="output/" + values['option'] + ".png")
            except:
                pass
            
            #Update list of events if there is a change between 'controllable' and 'uncontrollable'
            if event == 'controllable':
                self.janela.Element('selected_event').update(values = self.enabled_e)
                self.event_type = 'controllable'
            elif event == 'uncontrollable':
                self.janela.Element('selected_event').update(values = self.__not_cont_inputs)
                self.event_type = 'uncontrollable'
            elif event == 'trigger':
                # An event is triggered
                # print(f"trigger event: {values['selected_event']}")
                if values['controllable'] == True:
                    self.__events[values['selected_event']].call()
                else:
                    self.__receiver.receive_event(values['selected_event'])

        self.janela.Close()

    ###############################################################################################
    def events_trace(self):
        '''
            This method monitor the occurance of new events and get the enabled controllable events
        '''
        while True:
            g_var.trace_update_flag.acquire()
            while (g_var.events_trace.tail(1).empty) or (self.current_status_id == g_var.events_trace.tail(1).index[0]):
                g_var.trace_update_flag.wait()
            current_status = g_var.events_trace.tail(1)                 # Get the last update
            self.current_status_id = current_status.index[0]            # Set the id of the last event

            self.enabled_e = current_status['enabled_events'].array[0]

            # Update list of allowed controllable events
            if self.event_type == 'controllable':
                self.janela.Element('selected_event').update(values = self.enabled_e)

            #Update tracer

            g_var.trace_update_flag.release()                   # Release mutex