import time
from lib.Automaton import Automaton
from lib.StateMachine import StateMachine
from EVENTS import *

# Create and Start the State Machine
G1 = Automaton('Battery Monitor')
G1.read_xml('battery_monitor.xml')
SM = StateMachine(G1)
SM.start()

# The State Machine must be fully started before events occur
time.sleep(2)

# Call event execution
bat_OK.call()

bat_L.call()
bat_OK.call()
bat_L.call()
bat_OK.call()
bat_L.call()
bat_OK.call()

# while True:
    # e = input("Which is the event?\nEvent: ")
    # bat_L()
    # trigger_event(e)