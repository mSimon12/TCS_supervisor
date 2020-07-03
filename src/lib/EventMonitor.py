'''
    This library is responsible for monitoring all transitions that occur on the system.
    It allows the occurance of only one event at a time
'''

from threading import Condition

event_occured = Condition()
last_event = None

def trigger_event(event_name):
    '''
        Trigger the event and notify State Machines about it.
    '''
    global last_event, event_occured
    print("1- ",event_name, "triggered!\n")
    event_occured.acquire()                             # Acquire access to the event section
    last_event = event_name                             # Change the event
    try:
        event_occured.notifyAll()                       # Notify the occurence of a new event
    except RuntimeError:
        print("ERROR: Unable to notify new event!")
    event_occured.release()                             # Release access to the event section