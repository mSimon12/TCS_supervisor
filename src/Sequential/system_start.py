from lib.Automaton import MultiAutomata
from lib.StateMachine import StateMachine, Supervisor
from lib.ProductSystem import ProductSystem
from Intereface import EventInterface
from MissionManager import MissionManager
from lib.EventReceiver import EventReceiver

#############################################################################
#### Create Multiple State Machines from one file  #################
G = MultiAutomata('Plant')
G.read_xml('files/Plant.xml')         # File with multiple Automata
SM = {}
for aut in G.get_automata().values():
    SM[aut.get_name()] = StateMachine(aut)


#############################################################################
#### Create Multiple Supervisors from one file  ###################
S = MultiAutomata('Supervisors')
S.read_xml('files/Supervisors.xml')         # File with multiple Automata
SUP = {}
for aut in S.get_automata().values():
    SUP[aut.get_name()] = Supervisor(aut)


#############################################################################
#### Start Product System ###################################################
ps =  ProductSystem(SM, SUP)
ps.start()

#############################################################################
#### Start the Interface ####################################################
interface = EventInterface()
interface.start()

#############################################################################
#### Start the Mission Manager  #############################################
mm = MissionManager()
mm.start()

#############################################################################
#### Start the Events Receiver  #############################################
receiver = EventReceiver()

import time

time.sleep(3)
for i in range(0,10):
    receiver.receive_event('battery_low')
    receiver.receive_event('battery_verylow')
    receiver.receive_event('battery_low')
    receiver.receive_event('battery_ok')

