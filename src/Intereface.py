from threading import Thread
import PySimpleGUI as sg
from PIL import Image
import inspect

import handlers.EVENTS as events_module
import handlers.STATES as states_module

class EventInterface(Thread):

    def __init__(self):
        Thread.__init__(self)  

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

        #Layout
        layout =[ 
            [sg.Text('Current machine:'), sg.InputCombo(values=machines, default_value=machines[0], size=(35,10), key='option', enable_events=True)],
            [sg.Image("output/" + machines[0] + ".png", key="_IMAGE_", size=(1200,600), background_color="white")],
            [sg.Text('Trigger event')],
            [sg.Radio('Controllable','event_type', default=False, key='controllable',enable_events=True), sg.Radio('Uncontrollable','event_type', default=True, key='uncontrollable',enable_events=True)],
            [sg.InputCombo(values = self.not_cont_e, default_value= self.not_cont_e[0], size=(20,10), key='selected_event', enable_events=True), sg.Button('TRIGGER', key='trigger')]
        ]

        #Janela
        self.janela = sg.Window("State Machine visualizer", size=(1200,700)).layout(layout)
        
        
    def run(self):
        while True:
            #Extrair os dados da tela
            event, values = self.janela.Read(timeout=1000)
            if event in (None, 'Cancel'):   # if user closes window or clicks cancel
                print('\nCLOSING EVENT INTERFACE ...\n')
                break

            #Update the Automaton
            try:
                self.janela.Element("_IMAGE_").update(filename="output/" + values['option'] + ".png", size=(1200,600))
            except:
                pass
            
            if event == 'controllable':
                self.janela.Element('selected_event').update(values = self.cont_e)
            elif event == 'uncontrollable':
                self.janela.Element('selected_event').update(values = self.not_cont_e)
            elif event == 'trigger':
                print(f"trigger event: {values['selected_event']}")
                self.__events[values['selected_event']].call()
        self.janela.Close()
