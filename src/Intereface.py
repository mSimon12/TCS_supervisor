from threading import Thread
import PySimpleGUI as sg
from PIL import Image
import inspect
import os
import pandas as pd

from lib.EventReceiver import EventReceiver

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

        # Object to simulate non-controllable events
        self.__receiver = EventReceiver()

        # Get translation table
        filename = "OP/translation_table.csv"
        translation_table = pd.read_csv(filename)

        # Get name of the Machines
        machines = [s[0] for s in inspect.getmembers(states_module,inspect.isclass)]

        # Get all events call in the module
        self.__events = {}
        for x in inspect.getmembers(events_module,inspect.isclass):
            self.__events[x[0]] = x[1]  

        # Get controllable events
        self.cont_e = [e for e in self.__events if self.__events[e].is_controllable()]
       
        # Get uncontrollable events
        self.not_cont_e = [e for e in self.__events if not self.__events[e].is_controllable()]
        
        self.not_cont_inputs = []
        for hl_event in self.not_cont_e:
            self.not_cont_inputs.append(translation_table[(translation_table['high-level']==hl_event)]['low-level'].array[0])

        #Layout
        layout =[ 
            [sg.Text('Current machine:'), sg.InputCombo(values=machines, default_value=machines[0], size=(35,10), key='option', enable_events=True)],
            [sg.Image("output/" + machines[0] + ".png", key="_IMAGE_", background_color="white")],
            [sg.Text('Trigger event')],
            [sg.Radio('Controllable','event_type', default=False, key='controllable',enable_events=True), sg.Radio('Uncontrollable','event_type', default=True, key='uncontrollable',enable_events=True)],
            [sg.InputCombo(values = self.not_cont_inputs, default_value= self.not_cont_inputs[0], size=(20,10), key='selected_event', enable_events=True), sg.Button('TRIGGER', key='trigger')]
        ]

        #Janela
        self.janela = sg.Window("State Machine visualizer", size=(1000,500)).layout(layout)
        
        
    def run(self):
        while True:
            #Extrair os dados da tela
            event, values = self.janela.Read(timeout=1000)
            if event in (None, 'Cancel'):   # if user closes window or clicks cancel
                print('\nCLOSING EVENT INTERFACE ...\n')
                break

            #Update the Automaton
            try:
                self.janela.Element("_IMAGE_").update(filename="output/" + values['option'] + ".png")
            except:
                pass
            
            if event == 'controllable':
                self.janela.Element('selected_event').update(values = self.cont_e)
            elif event == 'uncontrollable':
                self.janela.Element('selected_event').update(values = self.not_cont_inputs)
            elif event == 'trigger':
                print(f"trigger event: {values['selected_event']}")
                if values['controllable'] == True:
                    self.__events[values['selected_event']].call()
                else:
                    self.__receiver.receive_event(values['selected_event'])
        self.janela.Close()
