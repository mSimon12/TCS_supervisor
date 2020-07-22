import inspect
from threading import Thread, Condition
import importlib
from datetime import datetime
import pandas as pd

######################################################################################################### 
# Global variables and mutexes
class g_var():
	SM_update_flag = Condition()			# Flag for SM signaling their update
	SM_status = {}							# Contain the status of all State Machines (False = not updated)
	
	new_event = Condition()				    # Flag to sinalize the occurance of a new event
	last_event = None						# Last occured event
	events_trace = pd.DataFrame(columns=['event', 'enabled_events', 'states', 'time'])		# Historic os all events
	trace_update_flag = Condition()
	
	# Events control related to SM update
	allow_events_flag = Condition()
	event_allowed = False

######################################################################################################### 
##### -- General event caller -- ########################################
def trigger_event(event, event_class, param):
	'''
		Function responsible for verifying if the required event is allowed to occur,
		after all State Machines are updated, and if it is allowed the handler (command)
		is executed.
	'''
	g_var.allow_events_flag.acquire()
	while g_var.event_allowed == False:
		g_var.allow_events_flag.wait()											# Wait till all State Machines are updated
	g_var.event_allowed = False													# Block occurance of another event
	g_var.allow_events_flag.release()

	#Verify if the current event is enabled by all SM that contain it
	if event_class.get_status() == True:
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
	

class EventsMonitor(Thread):
	'''
		Class responsible for monitoring the set of enabled events, last event and current states
	'''
	def __init__(self):
		Thread.__init__(self)

		# Get all controllable events into a list
		events_module = importlib.import_module("OP.EVENTS")
		self.__events = {}
		for x in inspect.getmembers(events_module, inspect.isclass):
			self.__events[x[0]]=x[1]
    
		self.__cont_e = [e for e in self.__events if self.__events[e].is_controllable()] 

	def run(self):
		while True:
			#Verify if all Machines are updated
			g_var.SM_update_flag.acquire()
			while (not all(g_var.SM_status.values()) or (not bool(g_var.SM_status))):
				g_var.SM_update_flag.wait()
			g_var.SM_status = {x: False for x in g_var.SM_status}				# Clear all State Machines status
			g_var.SM_update_flag.release()

			#Update events_trace
			time = datetime.now().strftime("%H:%M:%S")							# Get time
			g_var.events_trace = g_var.events_trace.append({
				"event" : g_var.last_event, 
				"enabled_events": [e for e in self.__cont_e if self.__events[e].get_status()], 
				"states":[], 
				"time": time}, ignore_index=True)		# Save the last event

			# Notify the trace update
			g_var.trace_update_flag.acquire()
			g_var.trace_update_flag.notifyAll()
			g_var.trace_update_flag.release()
			
			# Allow the occurance of a new event
			g_var.allow_events_flag.acquire()
			g_var.event_allowed = True
			g_var.allow_events_flag.notify()							 # Notify that an event can occur
			g_var.allow_events_flag.release()

