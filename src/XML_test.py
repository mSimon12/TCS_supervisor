import untangle as ut 
import xmltodict

obj = ut.parse('files/plant.xml')
# fd= open('battery_monitor.xml')
# doc = xmltodict.parse(fd.read())

# print(doc['Automata']['Automaton']['@name'])
# print(doc['Automata']['Automaton']['Events']['Event'][1])

a = obj.Automata.children

# x: (x['name'] == 'aproach') in obj.Automata.Automaton

for x in obj.Automata.Automaton:
    if x['name']=='approach':
        aut = x

# aut: aut in a 


print(len(obj.Automata))

# for state in obj.Automata.Automaton.States.children:
#     print("Oi")
#     print(state['name'])
