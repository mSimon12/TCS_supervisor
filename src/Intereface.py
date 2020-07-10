import PySimpleGUI as sg
import ast

class TelaPython(object):

    def __init__(self):

        filename = 'handlers/STATES.py'
        with open(filename) as file:
            node = ast.parse(file.read())
        classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
        machines = [] 
        for c in classes:
            machines.append(c.name)
        print(machines)

        #Layout
        layout =[ 
            [sg.Text('Current machine:'), sg.InputCombo(values=machines, default_value=machines[0], size=(25,10), key='option', enable_events=True)],
            [sg.Image("output/" + machines[0] + ".png", key="_IMAGE_")]
        ]

        #Janela
        self.janela = sg.Window("State Machine visualizer", size=(1000,500)).layout(layout)
        
        
    def Iniciar(self):
        while True:
            #Extrair os dados da tela
            event, values = self.janela.Read(timeout=1)
            if event in (None, 'Cancel'):   # if user closes window or clicks cancel
                break
            try:
                self.janela.Element("_IMAGE_").update(filename="output/" + values['option'] + ".png")
            except:
                pass

tela = TelaPython()
tela.Iniciar()