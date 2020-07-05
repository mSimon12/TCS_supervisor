from lib.Automaton import Automaton
from lib.StateMachine import StateMachine
from handlers.EVENTS import *

# Create and Start the State Machine
G1 = Automaton('Battery Monitor')
G1.read_xml('battery_monitor.xml')
SM = StateMachine(G1)
SM.start()

# Call event execution
bat_OK.call()

bat_L.call()
bat_LL.call()
bat_L.call()
bat_OK.call()

bat_L.call()
bat_OK.call()