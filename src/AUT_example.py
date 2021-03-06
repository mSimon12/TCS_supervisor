from lib.Automaton import Automaton, MultiAutomata
from lib.StateMachine import StateMachine, Supervisor
from OP.EVENTS import *
import time

##############################################################################
#### Create and Start one State Machine  #####################################

# G1 = Automaton('Battery Monitor')
# G1.read_xml('files/battery_monitor.xml')

# SM = StateMachine(G1)
# SM.start()


#### Create and Start Multiple State Machines from one file  #################

# G = MultiAutomata('Plant')
# G.read_xml('files/Plant.xml')         # File with multiple Automata
# SM = {}
# for aut in G.get_automata().values():
#     SM[aut.get_name()] = StateMachine(aut)

# #Start all State Machines
# for sm in SM.values():
#     sm.start()


##############################################################################
#### Create and Start one Supervisor  ########################################

# S = Automaton('Battery Monitor')
# S.read_xml('files/battery_monitor.xml')

# SM = Supervisor(S)
# SM.start()


#### Create and Start Multiple Supervisors from one file  ###################

# S = MultiAutomata('Supervisors')
# S.read_xml('files/Supervisors.xml')         # File with multiple Automata
# SUP = {}
# for aut in S.get_automata().values():
#     SUP[aut.get_name()] = Supervisor(aut)

# #Start all State Machines
# for sup in SUP.values():
#     sup.start()


#############################################################################
#### Call events execution ##################################################

st_app.call()

rst_app.call()

end_app.call()


