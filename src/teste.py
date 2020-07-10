from graphviz import Digraph
import time

from lib.Automaton import Automaton, MultiAutomata
from lib.StateMachine import StateMachine, Supervisor
from handlers.EVENTS import *

# #### Create and Start one State Machine  #####################################
# G1 = Automaton('approach')
# G1.read_xml('files/approach.xml')

x = {}
x['fill'] = 2
x['bod'] = 3

print(x)