from lib.Automaton import Automaton, MultiAutomata

################################################################
# Example for a file with only one Automaton
G1 = Automaton('Test_Automaton')

G1.insert_state("N1", idt=0, initial=True)
G1.insert_state("N2", idt=1)
G1.insert_state("N3", idt=2)

G1.insert_event("e1", idt=0)
G1.insert_event("e2", idt=1)

G1.insert_transition("N1","N2","e1")
G1.insert_transition("N2","N3","e1")
G1.insert_transition("N3","N1","e1")
G1.insert_transition("N1","N3","e2")
G1.insert_transition("N3","N2","e2")
G1.insert_transition("N2","N1","e2")

G1.show_states()
G1.show_events()
G1.show_transitions()

G1.export_automaton()