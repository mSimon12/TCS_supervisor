
from lib.Automaton import MultiAutomata
from lib.StateMachine import StateMachine, Supervisor
from MissionManager import MissionManager
from Intereface import EventInterface


#############################################################################
#### Create and Start Multiple State Machines from one file  #################
G = MultiAutomata('Plant')
G.read_xml('files/Plant.xml')         # File with multiple Automata
SM = {}
for aut in G.get_automata().values():
    SM[aut.get_name()] = StateMachine(aut)

#Start all State Machines
for sm in SM.values():
    sm.start()


#############################################################################
#### Create and Start Multiple Supervisors from one file  ###################
S = MultiAutomata('Supervisors')
S.read_xml('files/Supervisors.xml')         # File with multiple Automata
SUP = {}
for aut in S.get_automata().values():
    SUP[aut.get_name()] = Supervisor(aut)

#Start all State Machines
for sup in SUP.values():
    sup.start()

#############################################################################
#### Start the Interface ####################################################
ev = EventInterface()
ev.start()

#############################################################################
#### Start the Mission Manager  #############################################
mm = MissionManager()
mm.start()





