import untangle as ut 
import xmltodict

obj = ut.parse('battery_monitor.xml')
# fd= open('battery_monitor.xml')
# doc = xmltodict.parse(fd.read())

# print(doc['Automata']['Automaton']['@name'])
# print(doc['Automata']['Automaton']['Events']['Event'][1])

print(obj.Automata.Automaton.States.State)

for state in obj.Automata.Automaton.States.children:
    print("Oi")
    print(state['name'])
