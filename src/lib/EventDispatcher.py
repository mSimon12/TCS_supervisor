from threading import Thread, Condition

# Global variables and mutexes
class g_var:
	SM_status = {}
	SM_mutex = Condition()
	last_event = None
	req_SM_update = Condition()

##### -- General event caller -- ########################################
def trigger_event(event, event_class, param):
	'''
		Trigger event handler and notify State Machines about the event occured.
	'''
	g_var.SM_mutex.acquire()
	#Verify if all Machines are updated
	while (not all(g_var.SM_status.values()) or (not bool(g_var.SM_status))):
		g_var.SM_mutex.wait()

	#Verify if all SM enable this event
	g_var.req_SM_update.acquire()
	if event_class.get_status() == True:
		g_var.SM_status = {x: False for x in g_var.SM_status}	# Clear all SM status
		g_var.last_event = event
		h = Thread(target=event_class.handler, args=[param])
		h.start()
		h.join()

		# Notify State Machines the need of update
		try:
			g_var.req_SM_update.notifyAll()
		except RuntimeError:
			print('ERROR: Unable to notify new event!')
	else:
		print(event, ' not enabled!')
	g_var.req_SM_update.release()
	g_var.SM_mutex.release()