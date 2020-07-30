import inspect
import importlib
import pandas as pd
from datetime import datetime
from threading import Thread, Condition

import OP.EVENTS as events_module

######################################################################################################### 
##### -- Global variables and mutexes -- ################################################################
class g_var():
	events_trace = pd.DataFrame(columns=['event', 'enabled_events', 'states', 'time'])		# Historic os all events
	trace_update_flag = Condition()															# Flag for signaling the addition of a new event into the trace	

#########################################################
# Buffers and mutexes for controlling the Product System
cont_events_buffer = []										# Buffer with triggered controllable events
uncont_events_buffer = []									# Buffer with triggered uncontrollable events

add_event_mutex = Condition()								# Mutex for adding new events to the buffers
new_event_flag = Condition()								# Signal for the occurance af a new event

######################################################################################################### 
##### -- General event caller -- ########################################
def trigger_event(event, event_class, param):
	'''
		Functuon responsible for adding events on the buffer, it separates between controllable and
		uncontrollable events.
	'''
	add_event_mutex.acquire()
	if event_class.is_controllable():
		cont_events_buffer.append([event, event_class, param])
	else:
		uncont_events_buffer.append([event, event_class, param])
	
	new_event_flag.acquire()
	new_event_flag.notify()					# Notify that there is a new event on the buffer
	new_event_flag.release()

	add_event_mutex.release()

######################################################################################################### 
##### -- Product System -- ########################################
class ProductSystem(Thread):
	'''
		Class that executes the Product System.
		It executes the last triggered event, update the Plants, the Supervisors and the event trace.
	'''

	def __init__(self, plants, supervisors):
		Thread.__init__(self)
		self.__SMs = plants																		# Dictionary with all Sub-plants
		self.__SUPs = supervisors																# Dictionary with Modular Supervisors

		# Get all possible events names into a dictionary 
		self.__events = {}																		
		for x in inspect.getmembers(events_module, inspect.isclass):
			self.__events[x[0]]=x[1]
    
		self.__cont_e = [e for e in self.__events if self.__events[e].is_controllable()] 		# Get list of 'controllable' events names

		self.update_trace(None)																	# Update trace of events


	def run(self):
		while True:
			# Wait till there is a new event on any buffer
			new_event_flag.acquire()
			while (cont_events_buffer == []) and (uncont_events_buffer == []):
				new_event_flag.wait()
			new_event_flag.release()

			# Get next event on the buffer (uncontrollable events first)
			if uncont_events_buffer != []:
				event = uncont_events_buffer.pop(0)
				# event[1].handler(event[2])													# Call the execution of the handler
			elif cont_events_buffer != []:
				# Execute controllable event
				event = cont_events_buffer.pop(0)
				
				#Verify if the current event is enabled by all SM that contain it
				if event[1].get_status() == True:
					event[1].handler(event[2])												# Call the execution of the handler
				else:
					print("\nEvent '" + event[0] + "' is not enabled!")

			#Update plants
			for sm in self.__SMs:
				self.__SMs[sm].state_update(event[0])

			#Update supervisors
			for sup in self.__SUPs:
				self.__SUPs[sup].state_update(event[0])

			self.update_trace(event[0])														# Update trace of events


	def update_trace(self,event):
		'''
			Method responsible for adding the last occured event into the trace containing:
				- event name;
				- enabled events;
				- current states;
				- time.
		'''
		#Update events_trace
		time = datetime.now().strftime("%H:%M:%S")												# Get time
		
		# Get current states of all machines
		states = {}
		for s in self.__SMs:
			states[s] = self.__SMs[s].get_state()

		g_var.events_trace = g_var.events_trace.append({
			"event" : event, 																	# Save the last event
			"enabled_events": [e for e in self.__cont_e if self.__events[e].get_status()], 		# Save enabled events
			"states": states,																	# Save current states
			"time": time}, ignore_index=True)													# Save current time

		# Notify the update of the trace
		g_var.trace_update_flag.acquire()
		g_var.trace_update_flag.notifyAll()
		g_var.trace_update_flag.release()
		