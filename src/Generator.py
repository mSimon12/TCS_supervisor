from lib.Automaton import Automaton, MultiAutomata

# Example for a file with only one Automaton
# G1 = Automaton('Battery Monitor')
# G1.read_xml('files/battery_monitor.xml')
# G1.show_states()
# G1.show_events()
# G1.show_transitions()
# G1.show_automaton()

# # Generate a file with the events
# G1.gen_events_calls()

# # Generate a file with the states
# G1.gen_states_calls()

# Example for a file with multiple Automata
G = MultiAutomata('Plant')
G.read_xml('files/plant.xml')
G.generate_calls()

