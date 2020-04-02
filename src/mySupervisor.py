
from SCT import SupBuilder

sup1 = SupBuilder('mySupervisor')
# sup1.insert_state('A')
# sup1.insert_state('B')
# sup1.insert_state('C')
# sup1.insert_state('D')
# sup1.insert_state('E')
# sup1.insert_transition('t1','A','B')
# sup1.insert_transition('t2','A','D')
# sup1.insert_transition('t3','B','A')
# sup1.insert_transition('t4','B','C')
# sup1.insert_transition('t5','C','E')
# sup1.insert_transition('t1','D','D')
# sup1.insert_transition('t4','D','E')
# sup1.insert_transition('t3','E','A')
# sup1.insert_transition('t2','E','B')
sup1.read_csv('first.csv')

sup1.show_supervisor()

sup1.show_states()