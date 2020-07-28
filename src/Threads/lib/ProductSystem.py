import inspect
import importlib
import pandas as pd
from datetime import datetime
from threading import Thread, Condition


######################################################################################################### 
##### -- Global variables and mutexes -- ################################################################
class g_var():
	SM_update_flag = Condition()			# Flag for State Machines(SM) signaling their update
	SM_status = {}							# Variable that contain the update status of all State Machines (False = not updated)
	machines_current_state = {}				# Variable that contain the current state of each State Machine
	
	new_event = Condition()				    # Flag to sinalize the occurance of a new event to the SM
	last_event = None						# Last occured event

	events_trace = pd.DataFrame(columns=['event', 'enabled_events', 'states', 'time'])		# Historic os all events
	trace_update_flag = Condition()															# Flag for signaling the addition of a new event into the trace
	
	# Events control related to SM update
	allow_events_flag = Condition()
	event_allowed = False


######################################################################################################### 
##### -- General event caller -- ########################################
def trigger_event(event, event_class, param):
	'''
		This function execute the events calls according signals received from the EventsMonitor.
		It executes only one event by time by calling its handler on OP/EVENTS.py, which executes the 
		convertion from high-level events to low-level signals (commands).

		After the execution of each event, it signals to all State Machines the need of update. 
	'''
	# Wait till all State Machines have been updated
	g_var.allow_events_flag.acquire()
	while g_var.event_allowed == False:
		g_var.allow_events_flag.wait()											
	
	#Verify if the current event is enabled by all SM that contain it
	if event_class.get_status() == True:
		g_var.event_allowed = False											# Block occurance of another event
		g_var.new_event.acquire()											# Update last event occured
		g_var.last_event = event

		event_class.handler(param)											# Call the execution of the handler

		# Notify State Machines the need of update
		try:
			g_var.new_event.notifyAll()
		except RuntimeError:
			print('ERROR: Unable to notify new event!')
		
		g_var.new_event.release()											# Release mutexes
	else:
		print(event, ' not enabled!')										# Current controllable event not allowed by the system

	g_var.allow_events_flag.release()
	

######################################################################################################### 
##### -- Global variables and mutexes -- ################################################################
class EventsMonitor(Thread):
	'''
		Class responsible for monitoring if all State Machines have updated their status, if True, it 
		allows the occurance of a new event.

		It also is responsible for adding the last occured event into the trace containing:
			- event name;
			- enabled events;
			- current states;
			- time.
	'''
	def __init__(self, SM_number = 1):
		'''
			SM_number = quantity of Automata that may start before executing the EventsMonitor.
		'''
		Thread.__init__(self)

		# Get all controllable events into a list
		events_module = importlib.import_module("OP.EVENTS")
		self.__events = {}
		for x in inspect.getmembers(events_module, inspect.isclass):
			self.__events[x[0]]=x[1]
		self.SM_quantity = SM_number
    
		self.__cont_e = [e for e in self.__events if self.__events[e].is_controllable()] 		#Get list of controllable events

	def run(self):
		while True:
			#Verify if all Machines have been updated
			g_var.SM_update_flag.acquire()
			while (not all(g_var.SM_status.values())) or (len(g_var.SM_status) < self.SM_quantity):
				g_var.SM_update_flag.wait()
			g_var.SM_status = {x: False for x in g_var.SM_status}				# Clear all State Machines status
			g_var.SM_update_flag.release()

			#Update events_trace
			time = datetime.now().strftime("%H:%M:%S")							# Get time
			g_var.events_trace = g_var.events_trace.append({
				"event" : g_var.last_event, 														# Save the last event
				"enabled_events": [e for e in self.__cont_e if self.__events[e].get_status()], 		# Save enabled events
				"states": g_var.machines_current_state,												# Save current states
				"time": time}, ignore_index=True)													# Save current time

			# Notify the update of the trace
			g_var.trace_update_flag.acquire()
			g_var.trace_update_flag.notifyAll()
			g_var.trace_update_flag.release()
			
			# Allow the occurance of a new event
			g_var.allow_events_flag.acquire()
			g_var.event_allowed = True
			g_var.allow_events_flag.notify()				# Notify that an event can occur
			g_var.allow_events_flag.release()
