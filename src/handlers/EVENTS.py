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


##### -- abort_app call & handler -- ########################################
class abort_app:
	__enabled = {}

	def call(param = None):
		trigger_event('abort_app', abort_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event abort_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_app.__enabled.values())

	def set_status(name, status):
		abort_app.__enabled[name] = status


##### -- end_app call & handler -- ########################################
class end_app:
	__enabled = {}

	def call(param = None):
		trigger_event('end_app', end_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event end_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_app.__enabled.values())

	def set_status(name, status):
		end_app.__enabled[name] = status


##### -- er_app call & handler -- ########################################
class er_app:
	__enabled = {}

	def call(param = None):
		trigger_event('er_app', er_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_app.__enabled.values())

	def set_status(name, status):
		er_app.__enabled[name] = status


##### -- rsm_app call & handler -- ########################################
class rsm_app:
	__enabled = {}

	def call(param = None):
		trigger_event('rsm_app', rsm_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rsm_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_app.__enabled.values())

	def set_status(name, status):
		rsm_app.__enabled[name] = status


##### -- rst_app call & handler -- ########################################
class rst_app:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_app', rst_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_app.__enabled.values())

	def set_status(name, status):
		rst_app.__enabled[name] = status


##### -- st_app call & handler -- ########################################
class st_app:
	__enabled = {}

	def call(param = None):
		trigger_event('st_app', st_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event st_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_app.__enabled.values())

	def set_status(name, status):
		st_app.__enabled[name] = status


##### -- sus_app call & handler -- ########################################
class sus_app:
	__enabled = {}

	def call(param = None):
		trigger_event('sus_app', sus_app.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event sus_app...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_app.__enabled.values())

	def set_status(name, status):
		sus_app.__enabled[name] = status


##### -- bat_L call & handler -- ########################################
class bat_L:
	__enabled = {}

	def call(param = None):
		trigger_event('bat_L', bat_L.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event bat_L...')
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
		print('Executing event bat_LL...')
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
		print('Executing event bat_OK...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_OK.__enabled.values())

	def set_status(name, status):
		bat_OK.__enabled[name] = status


##### -- call_tele call & handler -- ########################################
class call_tele:
	__enabled = {}

	def call(param = None):
		trigger_event('call_tele', call_tele.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event call_tele...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(call_tele.__enabled.values())

	def set_status(name, status):
		call_tele.__enabled[name] = status


##### -- no_rb_pref call & handler -- ########################################
class no_rb_pref:
	__enabled = {}

	def call(param = None):
		trigger_event('no_rb_pref', no_rb_pref.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event no_rb_pref...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(no_rb_pref.__enabled.values())

	def set_status(name, status):
		no_rb_pref.__enabled[name] = status


##### -- rb_pref call & handler -- ########################################
class rb_pref:
	__enabled = {}

	def call(param = None):
		trigger_event('rb_pref', rb_pref.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rb_pref...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rb_pref.__enabled.values())

	def set_status(name, status):
		rb_pref.__enabled[name] = status


##### -- rep_gas call & handler -- ########################################
class rep_gas:
	__enabled = {}

	def call(param = None):
		trigger_event('rep_gas', rep_gas.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rep_gas...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rep_gas.__enabled.values())

	def set_status(name, status):
		rep_gas.__enabled[name] = status


##### -- rep_victim call & handler -- ########################################
class rep_victim:
	__enabled = {}

	def call(param = None):
		trigger_event('rep_victim', rep_victim.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rep_victim...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rep_victim.__enabled.values())

	def set_status(name, status):
		rep_victim.__enabled[name] = status


##### -- req_assist call & handler -- ########################################
class req_assist:
	__enabled = {}

	def call(param = None):
		trigger_event('req_assist', req_assist.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event req_assist...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(req_assist.__enabled.values())

	def set_status(name, status):
		req_assist.__enabled[name] = status


##### -- abort_exp call & handler -- ########################################
class abort_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('abort_exp', abort_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event abort_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_exp.__enabled.values())

	def set_status(name, status):
		abort_exp.__enabled[name] = status


##### -- end_exp call & handler -- ########################################
class end_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('end_exp', end_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event end_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_exp.__enabled.values())

	def set_status(name, status):
		end_exp.__enabled[name] = status


##### -- er_exp call & handler -- ########################################
class er_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('er_exp', er_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_exp.__enabled.values())

	def set_status(name, status):
		er_exp.__enabled[name] = status


##### -- rsm_exp call & handler -- ########################################
class rsm_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('rsm_exp', rsm_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rsm_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_exp.__enabled.values())

	def set_status(name, status):
		rsm_exp.__enabled[name] = status


##### -- rst_exp call & handler -- ########################################
class rst_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_exp', rst_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_exp.__enabled.values())

	def set_status(name, status):
		rst_exp.__enabled[name] = status


##### -- st_exp call & handler -- ########################################
class st_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('st_exp', st_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event st_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_exp.__enabled.values())

	def set_status(name, status):
		st_exp.__enabled[name] = status


##### -- sus_exp call & handler -- ########################################
class sus_exp:
	__enabled = {}

	def call(param = None):
		trigger_event('sus_exp', sus_exp.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event sus_exp...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_exp.__enabled.values())

	def set_status(name, status):
		sus_exp.__enabled[name] = status


##### -- critic_fail call & handler -- ########################################
class critic_fail:
	__enabled = {}

	def call(param = None):
		trigger_event('critic_fail', critic_fail.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event critic_fail...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(critic_fail.__enabled.values())

	def set_status(name, status):
		critic_fail.__enabled[name] = status


##### -- fail call & handler -- ########################################
class fail:
	__enabled = {}

	def call(param = None):
		trigger_event('fail', fail.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event fail...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(fail.__enabled.values())

	def set_status(name, status):
		fail.__enabled[name] = status


##### -- pos_fail call & handler -- ########################################
class pos_fail:
	__enabled = {}

	def call(param = None):
		trigger_event('pos_fail', pos_fail.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event pos_fail...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(pos_fail.__enabled.values())

	def set_status(name, status):
		pos_fail.__enabled[name] = status


##### -- rst_f call & handler -- ########################################
class rst_f:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_f', rst_f.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_f...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_f.__enabled.values())

	def set_status(name, status):
		rst_f.__enabled[name] = status


##### -- er_gs call & handler -- ########################################
class er_gs:
	__enabled = {}

	def call(param = None):
		trigger_event('er_gs', er_gs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_gs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_gs.__enabled.values())

	def set_status(name, status):
		er_gs.__enabled[name] = status


##### -- gas_found call & handler -- ########################################
class gas_found:
	__enabled = {}

	def call(param = None):
		trigger_event('gas_found', gas_found.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event gas_found...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(gas_found.__enabled.values())

	def set_status(name, status):
		gas_found.__enabled[name] = status


##### -- off_gs call & handler -- ########################################
class off_gs:
	__enabled = {}

	def call(param = None):
		trigger_event('off_gs', off_gs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event off_gs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(off_gs.__enabled.values())

	def set_status(name, status):
		off_gs.__enabled[name] = status


##### -- on_gs call & handler -- ########################################
class on_gs:
	__enabled = {}

	def call(param = None):
		trigger_event('on_gs', on_gs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event on_gs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(on_gs.__enabled.values())

	def set_status(name, status):
		on_gs.__enabled[name] = status


##### -- rst_gs call & handler -- ########################################
class rst_gs:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_gs', rst_gs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_gs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_gs.__enabled.values())

	def set_status(name, status):
		rst_gs.__enabled[name] = status


##### -- move_to call & handler -- ########################################
class move_to:
	__enabled = {}

	def call(param = None):
		trigger_event('move_to', move_to.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event move_to...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(move_to.__enabled.values())

	def set_status(name, status):
		move_to.__enabled[name] = status


##### -- abort_rb call & handler -- ########################################
class abort_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('abort_rb', abort_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event abort_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_rb.__enabled.values())

	def set_status(name, status):
		abort_rb.__enabled[name] = status


##### -- end_rb call & handler -- ########################################
class end_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('end_rb', end_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event end_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_rb.__enabled.values())

	def set_status(name, status):
		end_rb.__enabled[name] = status


##### -- er_rb call & handler -- ########################################
class er_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('er_rb', er_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_rb.__enabled.values())

	def set_status(name, status):
		er_rb.__enabled[name] = status


##### -- rsm_rb call & handler -- ########################################
class rsm_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('rsm_rb', rsm_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rsm_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_rb.__enabled.values())

	def set_status(name, status):
		rsm_rb.__enabled[name] = status


##### -- rst_rb call & handler -- ########################################
class rst_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_rb', rst_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_rb.__enabled.values())

	def set_status(name, status):
		rst_rb.__enabled[name] = status


##### -- st_rb call & handler -- ########################################
class st_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('st_rb', st_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event st_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_rb.__enabled.values())

	def set_status(name, status):
		st_rb.__enabled[name] = status


##### -- sus_rb call & handler -- ########################################
class sus_rb:
	__enabled = {}

	def call(param = None):
		trigger_event('sus_rb', sus_rb.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event sus_rb...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_rb.__enabled.values())

	def set_status(name, status):
		sus_rb.__enabled[name] = status


##### -- end_tele call & handler -- ########################################
class end_tele:
	__enabled = {}

	def call(param = None):
		trigger_event('end_tele', end_tele.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event end_tele...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_tele.__enabled.values())

	def set_status(name, status):
		end_tele.__enabled[name] = status


##### -- er_tele call & handler -- ########################################
class er_tele:
	__enabled = {}

	def call(param = None):
		trigger_event('er_tele', er_tele.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_tele...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_tele.__enabled.values())

	def set_status(name, status):
		er_tele.__enabled[name] = status


##### -- rst_tele call & handler -- ########################################
class rst_tele:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_tele', rst_tele.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_tele...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_tele.__enabled.values())

	def set_status(name, status):
		rst_tele.__enabled[name] = status


##### -- st_tele call & handler -- ########################################
class st_tele:
	__enabled = {}

	def call(param = None):
		trigger_event('st_tele', st_tele.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event st_tele...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_tele.__enabled.values())

	def set_status(name, status):
		st_tele.__enabled[name] = status


##### -- abort_vsv call & handler -- ########################################
class abort_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('abort_vsv', abort_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event abort_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_vsv.__enabled.values())

	def set_status(name, status):
		abort_vsv.__enabled[name] = status


##### -- end_vsv call & handler -- ########################################
class end_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('end_vsv', end_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event end_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_vsv.__enabled.values())

	def set_status(name, status):
		end_vsv.__enabled[name] = status


##### -- er_vsv call & handler -- ########################################
class er_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('er_vsv', er_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_vsv.__enabled.values())

	def set_status(name, status):
		er_vsv.__enabled[name] = status


##### -- rsm_vsv call & handler -- ########################################
class rsm_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('rsm_vsv', rsm_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rsm_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_vsv.__enabled.values())

	def set_status(name, status):
		rsm_vsv.__enabled[name] = status


##### -- rst_vsv call & handler -- ########################################
class rst_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_vsv', rst_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_vsv.__enabled.values())

	def set_status(name, status):
		rst_vsv.__enabled[name] = status


##### -- st_vsv call & handler -- ########################################
class st_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('st_vsv', st_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event st_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_vsv.__enabled.values())

	def set_status(name, status):
		st_vsv.__enabled[name] = status


##### -- sus_vsv call & handler -- ########################################
class sus_vsv:
	__enabled = {}

	def call(param = None):
		trigger_event('sus_vsv', sus_vsv.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event sus_vsv...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_vsv.__enabled.values())

	def set_status(name, status):
		sus_vsv.__enabled[name] = status


##### -- er_vs call & handler -- ########################################
class er_vs:
	__enabled = {}

	def call(param = None):
		trigger_event('er_vs', er_vs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event er_vs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_vs.__enabled.values())

	def set_status(name, status):
		er_vs.__enabled[name] = status


##### -- off_vs call & handler -- ########################################
class off_vs:
	__enabled = {}

	def call(param = None):
		trigger_event('off_vs', off_vs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event off_vs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(off_vs.__enabled.values())

	def set_status(name, status):
		off_vs.__enabled[name] = status


##### -- on_vs call & handler -- ########################################
class on_vs:
	__enabled = {}

	def call(param = None):
		trigger_event('on_vs', on_vs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event on_vs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(on_vs.__enabled.values())

	def set_status(name, status):
		on_vs.__enabled[name] = status


##### -- rst_vs call & handler -- ########################################
class rst_vs:
	__enabled = {}

	def call(param = None):
		trigger_event('rst_vs', rst_vs.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event rst_vs...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_vs.__enabled.values())

	def set_status(name, status):
		rst_vs.__enabled[name] = status


##### -- victim_found call & handler -- ########################################
class victim_found:
	__enabled = {}

	def call(param = None):
		trigger_event('victim_found', victim_found.__handler, param)

	def __handler(param = None):
		#Write code here...
		print('Executing event victim_found...')
		pass

	def get_status():
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(victim_found.__enabled.values())

	def set_status(name, status):
		victim_found.__enabled[name] = status