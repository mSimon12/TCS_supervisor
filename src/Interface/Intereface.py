import PySimpleGUI as sg

class TelaPython(object):

    def __init__(self):
        #Layout
        layout =[ 
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'),sg.Checkbox('Outlook', key='outlook'),sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'), sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h', size=(15,20), key='slider_vel')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]

        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        
        
    def Iniciar(self):
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            gmail_status = self.values['gmail']
            out_status = self.values['outlook']
            yahoo_status = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            vel = self.values['slider_vel']
            
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {gmail_status}')
            print(f'Aceita Outlook: {out_status}')
            print(f'Aceita Yahoo: {yahoo_status}')

            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade: {vel}')

tela = TelaPython()
tela.Iniciar()