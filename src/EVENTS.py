from threading import Thread, Condition

# Global variables and mutexes
class g_var:
	SM_status = {}
	SM_mutex = Condition()
	last_event = None
	req_SM_update = Condition()

##### -- General event caller -- ########################################
def trigger_event(event, handler, param):
	'''
		Trigger event handler and notify State Machines about the event occured.
	'''
	g_var.SM_mutex.acquire()
	#Verify if all Machines are updated
	while (not all(g_var.SM_status.values()) or (not bool(g_var.SM_status))):
		g_var.SM_mutex.wait()

	#Verify if all SM enable this event
	g_var.req_SM_update.acquire()
	if eval(event).get_status() == True:
		g_var.SM_status = {x: False for x in g_var.SM_status}	# Clear all SM status
		g_var.last_event = event
		h = Thread(target=handler, args=[param])
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


##### -- bat_L call & handler -- ########################################
class bat_L:
	__enabled = {}

	def call(param = None):
		trigger_event('bat_L', bat_L.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing bat_L...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_L.__enabled.values())

	def set_status(name, status):
		bat_L.__enabled[name] = status


##### -- bat_LL call & handler -- ########################################
class bat_LL:
	__enabled = {}

	def call(param = None):
		trigger_event('bat_LL', bat_LL.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing bat_LL...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_LL.__enabled.values())

	def set_status(name, status):
		bat_LL.__enabled[name] = status


##### -- bat_OK call & handler -- ########################################
class bat_OK:
	__enabled = {}

	def call(param = None):
		trigger_event('bat_OK', bat_OK.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing bat_OK...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_OK.__enabled.values())

	def set_status(name, status):
		bat_OK.__enabled[name] = status