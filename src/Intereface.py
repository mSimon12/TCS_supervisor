import os
import inspect
import pandas as pd
import PySimpleGUI as sg
from threading import Thread

from lib.EventReceiver import EventReceiver
from lib.ProductSystem import g_var, trigger_event

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

        #################################################################################
        #### -- Auxiliary variables -- ##################################################
        
        # Control of the tracer
        self.current_status_id = -1
        self.new_trace = False

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
        self.translation_table = pd.read_csv(filename)
        
        # Object to simulate non-controllable events
        self.__receiver = EventReceiver()

        #################################################################################
        #### -- Layout of the Window -- #################################################
        layout =[ 
            [sg.Text('Current machine:'), 
             sg.InputCombo(values=machines, default_value=machines[0], size=(35,10), key='option', enable_events=True)],

            [sg.Image("output/" + machines[0] + ".png", key="_IMAGE_", background_color="white")],

            [sg.Frame('Trace:',[
                [sg.Text("Id"), sg.Text("Event"), sg.Text("Parameters"),sg.Text("Time")],
                [sg.Multiline(size=(50,10), key='tracer', disabled=True, autoscroll=True)],
                [sg.SaveAs("SAVE", key='save', file_types = (("ALL Files", "*.*"),("CSV text",".csv")), enable_events=True),
                    sg.Button("REFRESH", key='refresh')]
                ]),
            
            sg.Frame('Trigger event',[
                [sg.Column([
                    [sg.Radio('Controllable','event_type', default=False, key='controllable',enable_events=True)], 
                    [sg.Radio('Uncontrollable','event_type', default=True, key='uncontrollable',enable_events=True)],
                    [sg.InputCombo(values = self.__not_cont_e, default_value= self.__not_cont_e[0], size=(20,10), key='selected_event', enable_events=True)],
                    [sg.Button('TRIGGER', key='trigger')]
                    ]),
                sg.VerticalSeparator(),
                sg.Column([
                    [sg.Text('Parameters:')],
                    [sg.Input(key='new_param',enable_events=True, size=(16,5)),
                        sg.Button("+", key='add_param', size=(1,1), button_color=('white','green'))],
                    [sg.Listbox('', key='param_list', size=(20, 4))],
                    [sg.Button("-", key='remove_param', size=(18,1), button_color=('white','red'))]
                    ])
                ]])
            ]
        ]
        
        # start the Window
        self.window = sg.Window("State Machine visualizer", size=(1000,600)).layout(layout)
        
        
    def run(self):
        self.event_type = 'uncontrollable'                                  # Event type selected on Radio
        self.enabled_e = []                                                 # List of enabled events
        self.param = []                                                     # Parameters of the event
        trace = Thread(target=self.events_trace)                            # Thread for the tracer monitor
        trace.start()                                                       # Start event tracer as a thread

        while True:
            #Get data from the Window
            event, values = self.window.Read(timeout=10)
            if event in (None, 'Cancel'):                                   # If user closes window or clicks cancel
                print('\nCLOSING EVENT INTERFACE ...\n')
                break

            # New event occured on the Prodct System
            if self.new_trace==True:
                self.new_trace = False
                #Update tracer screen
                if self.trace.tail(1).index[0] > 0:
                    if self.__events[self.trace.tail(1)['event'].values[0]].is_controllable():
                        color = 'blue'
                    else:
                        color = 'red'
                    text = self.trace.tail(1).drop(columns=['enabled_events','states']).to_string(header=False, justify='left')
                    self.window['tracer'].print(text, text_color=color)

                #Update the Automaton Image
                try:
                    self.window.Element("_IMAGE_").update(filename="output/" + values['option'] + ".png")
                except:
                    pass

            if event == 'option':
                #Update the Automaton Image
                try:
                    self.window.Element("_IMAGE_").update(filename="output/" + values['option'] + ".png")
                except:
                    pass

            elif event == 'controllable':
                #Show list of enabled controllable events
                self.window.Element('selected_event').update(values = self.enabled_e)
                self.event_type = 'controllable'

            elif event == 'uncontrollable':
                #Show list of uncontrollable events
                self.window.Element('selected_event').update(values = self.__not_cont_e)
                self.event_type = 'uncontrollable'

            elif event == 'trigger':
                # An event is triggered
                if values['controllable'] == True:
                    trigger_event(values['selected_event'], self.param)                             # Call the execution of the controllable event
                else:
                    # Trigger uncontrollable events
                    event = values['selected_event']

                    # Translate non-controllable events to low-level call
                    ll_event = self.translation_table[(self.translation_table['high-level']==event)]['low-level'].array[0]
                    self.__receiver.receive_event(ll_event, self.param)
                
                self.param = []                                                                     # Clear param
                self.window['param_list'].Update(values=self.param)                                 # Clear param screen

            elif event == 'refresh':
                self.window['tracer'].update('')
                #Refresh tracer
                if not self.trace.empty: 
                    for i in self.trace.iloc[1:].index:
                        if self.__events[self.trace.at[i,'event']].is_controllable():
                            color = 'blue'
                        else:
                            color = 'red'
                        text = self.trace.loc[[i]].drop(columns=['enabled_events','states']).to_string(header=False, justify='left')
                        self.window['tracer'].print(text, text_color=color)
            
            elif event == 'save':
                # Save content of tracer into a csv file
                filename = values['save']
                if '.' not in filename:
                    filename += ".csv"

                if '.csv' in filename:
                    
                    self.trace.drop(columns=['enabled_events','states']).to_csv(filename)
                else:
                    sg.Popup('Wrong file extension!', title='Saving failure!')
                print("saving")

            elif event == 'add_param':
                # Add a new item as parameter for the event
                # if values['new_param']:
                try:
                    self.param.append(eval(values['new_param'])) 
                    self.window['new_param'].update('')
                    self.window['param_list'].Update(values=self.param)
                except:
                    pass

            elif event == 'remove_param':
                # Remove an item from the list of parameters
                item = self.window['param_list'].GetIndexes()[0]
                self.param.pop(item)
                self.window['param_list'].Update(values=self.param)
                
        self.window.Close()


    ###############################################################################################
    def events_trace(self):
        '''
            This method monitor the occurance of new events on the Product System 
            and get the enabled controllable events.
        '''
        while True:
            # Wait a new event to be added to the tracer
            g_var.trace_update_flag.acquire()
            while (g_var.events_trace.tail(1).empty) or (self.current_status_id == g_var.events_trace.tail(1).index[0]):
                g_var.trace_update_flag.wait()

            self.trace = g_var.events_trace                                  # Get the last update
            self.current_status_id = self.trace.tail(1).index[0]             # Set the id of the last event

            self.new_trace = True                                            # Set new trace to True for update on the window
            self.enabled_e = self.trace.tail(1)['enabled_events'].array[0]   # Update list of enabled events

            # Update list of allowed controllable events showed on screen
            if self.event_type == 'controllable':
                self.window['selected_event'].update(values = self.enabled_e)

            g_var.trace_update_flag.release()                   # Release mutex