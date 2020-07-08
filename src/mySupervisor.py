from lib.Automaton import Automaton, MultiAutomata
from lib.StateMachine import StateMachine
from handlers.EVENTS import *

# Create and Start the State Machine
# G1 = Automaton('Battery Monitor')
# G1.read_xml('files/battery_monitor.xml')

# G2 = Automaton('Approach')
# G2.read_xml('files/approach.xml')

# SM1 = StateMachine(G1)
# SM2 = StateMachine(G2)

# SM1.start()
# SM2.start()

G = MultiAutomata('Plant')
G.read_xml('files/plant.xml')

SM = {}

#Create all State Machines 
for aut in G.get_automata().values():
    SM[aut.get_name()] = StateMachine(aut)

#Start all State Machines
for sm in SM.values():
    sm.start()

# Call event execution
bat_OK.call()

# bat_L.call()
# bat_LL.call()

st_app.call()

rsm_app.call()
# st_app.call()

# bat_L.call()
# bat_OK.call()

# end_app.call()

# bat_L.call()
# bat_OK.call()