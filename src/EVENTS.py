from threading import Thread, Condition
from lib.EventMonitor import trigger_event



##### -- bat_L call & handler -- ########################################
class bat_L:
	__count = 0
	__enableCond = Condition()
	__enabled = {}

	def call(param = None):
		bat_L.__enableCond.acquire()
		#Verify if all Machines are updated
		while bat_L.__count < len(bat_L.__enabled):
			bat_L.__enableCond.wait()
		bat_L.__count = 0
		print("3 - bat_L allowed")
		if all(bat_L.__enabled.values()) == True:
			trigger_event('bat_L')
			h = Thread(target=bat_L.__handler, args=[param])
			h.start()
		else:
			print('bat_L not enabled!')
		bat_L.__enableCond.release()

	def __handler(param = None):
		#Write code here...
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_L.__enabled.values())

	def set_status(name, status):
		bat_L.__enableCond.acquire()
		bat_L.__enabled[name] = status
		bat_L.__count += 1
		bat_L.__enableCond.notify()
		bat_L.__enableCond.release()


##### -- bat_LL call & handler -- ########################################
class bat_LL:
	__count = 0
	__enableCond = Condition()
	__enabled = {}

	def call(param = None):
		bat_LL.__enableCond.acquire()
		#Verify if all Machines are updated
		while bat_LL.__count < len(bat_LL.__enabled):
			bat_LL.__enableCond.wait()
		bat_LL.__count = 0
		print("3 - bat_LL allowed")
		if all(bat_LL.__enabled.values()) == True:
			trigger_event('bat_LL')
			h = Thread(target=bat_LL.__handler, args=[param])
			h.start()
		else:
			print('bat_LL not enabled!')
		bat_LL.__enableCond.release()

	def __handler(param = None):
		#Write code here...
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_LL.__enabled.values())

	def set_status(name, status):
		bat_LL.__enableCond.acquire()
		bat_LL.__enabled[name] = status
		bat_LL.__count += 1
		bat_LL.__enableCond.notify()
		bat_LL.__enableCond.release()


##### -- bat_OK call & handler -- ########################################
class bat_OK:
	__count = 0
	__enableCond = Condition()
	__enabled = {}

	def call(param = None):
		bat_OK.__enableCond.acquire()
		#Verify if all Machines are updated
		while bat_OK.__count < len(bat_OK.__enabled):
			bat_OK.__enableCond.wait()
		bat_OK.__count = 0
		print("3 - bat_OK allowed")
		if all(bat_OK.__enabled.values()) == True:
			trigger_event('bat_OK')
			h = Thread(target=bat_OK.__handler, args=[param])
			h.start()
		else:
			print('bat_OK not enabled!')
		bat_OK.__enableCond.release()

	def __handler(param = None):
		#Write code here...
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_OK.__enabled.values())

	def set_status(name, status):
		bat_OK.__enableCond.acquire()
		bat_OK.__enabled[name] = status
		bat_OK.__count += 1
		bat_OK.__enableCond.notify()
		bat_OK.__enableCond.release()