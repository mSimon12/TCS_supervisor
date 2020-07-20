from threading import Condition

# Global variables and mutexes
class g_var:
	SM_status = {}							# Contain the status of all State Machines (False = not updated)
	SM_mutex = Condition()					# Mutex for the SM_status variable
	last_event = None						# Last occured event
	req_SM_update = Condition()				# Mutex to disable event trigger while State Machines updating


##### -- General event caller -- ########################################
def trigger_event(event, event_class, param):
	'''
		Function responsible for verifying if the required event is allowed to occur,
		after all State Machines are updated, and if it is allowed the handler (command)
		is executed.
	'''
	g_var.SM_mutex.acquire()

	#Verify if all Machines are updated
	while (not all(g_var.SM_status.values()) or (not bool(g_var.SM_status))):
		g_var.SM_mutex.wait()

	g_var.req_SM_update.acquire()											# Block State Machine updating

	#Verify if the current event is enabled by all SM that contain it
	if event_class.get_status() == True:
		g_var.SM_status = {x: False for x in g_var.SM_status}				# Clear all State Machines status
		g_var.last_event = event											# Save the last event
		
		event_class.handler(param)											# Call the execution of the handler

		# Notify State Machines the need of update
		try:
			g_var.req_SM_update.notifyAll()
		except RuntimeError:
			print('ERROR: Unable to notify new event!')
	else:
		print(event, ' not enabled!')										# Current controllable event not allowed by the system
	
	# Release mutexes
	g_var.req_SM_update.release()
	g_var.SM_mutex.release()