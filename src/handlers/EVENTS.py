from lib.EventDispatcher import trigger_event

##### -- abort_app call & handler -- ########################################
class abort_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('abort_app', abort_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event abort_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		abort_app.__enabled[name] = status


##### -- end_app call & handler -- ########################################
class end_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('end_app', end_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event end_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		end_app.__enabled[name] = status


##### -- er_app call & handler -- ########################################
class er_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_app', er_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_app.__enabled[name] = status


##### -- rsm_app call & handler -- ########################################
class rsm_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rsm_app', rsm_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rsm_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rsm_app.__enabled[name] = status


##### -- rst_app call & handler -- ########################################
class rst_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_app', rst_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_app.__enabled[name] = status


##### -- st_app call & handler -- ########################################
class st_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('st_app', st_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event st_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		st_app.__enabled[name] = status


##### -- sus_app call & handler -- ########################################
class sus_app(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('sus_app', sus_app, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event sus_app...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_app.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		sus_app.__enabled[name] = status


##### -- bat_L call & handler -- ########################################
class bat_L(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('bat_L', bat_L, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event bat_L...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_L.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		bat_L.__enabled[name] = status


##### -- bat_LL call & handler -- ########################################
class bat_LL(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('bat_LL', bat_LL, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event bat_LL...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_LL.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		bat_LL.__enabled[name] = status


##### -- bat_OK call & handler -- ########################################
class bat_OK(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('bat_OK', bat_OK, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event bat_OK...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(bat_OK.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		bat_OK.__enabled[name] = status


##### -- call_tele call & handler -- ########################################
class call_tele(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('call_tele', call_tele, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event call_tele...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(call_tele.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		call_tele.__enabled[name] = status


##### -- no_rb_pref call & handler -- ########################################
class no_rb_pref(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('no_rb_pref', no_rb_pref, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event no_rb_pref...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(no_rb_pref.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		no_rb_pref.__enabled[name] = status


##### -- rb_pref call & handler -- ########################################
class rb_pref(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rb_pref', rb_pref, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rb_pref...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rb_pref.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rb_pref.__enabled[name] = status


##### -- rep_gas call & handler -- ########################################
class rep_gas(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rep_gas', rep_gas, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rep_gas...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rep_gas.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rep_gas.__enabled[name] = status


##### -- rep_victim call & handler -- ########################################
class rep_victim(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rep_victim', rep_victim, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rep_victim...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rep_victim.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rep_victim.__enabled[name] = status


##### -- req_assist call & handler -- ########################################
class req_assist(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('req_assist', req_assist, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event req_assist...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(req_assist.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		req_assist.__enabled[name] = status


##### -- abort_exp call & handler -- ########################################
class abort_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('abort_exp', abort_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event abort_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		abort_exp.__enabled[name] = status


##### -- end_exp call & handler -- ########################################
class end_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('end_exp', end_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event end_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		end_exp.__enabled[name] = status


##### -- er_exp call & handler -- ########################################
class er_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_exp', er_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_exp.__enabled[name] = status


##### -- rsm_exp call & handler -- ########################################
class rsm_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rsm_exp', rsm_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rsm_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rsm_exp.__enabled[name] = status


##### -- rst_exp call & handler -- ########################################
class rst_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_exp', rst_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_exp.__enabled[name] = status


##### -- st_exp call & handler -- ########################################
class st_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('st_exp', st_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event st_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		st_exp.__enabled[name] = status


##### -- sus_exp call & handler -- ########################################
class sus_exp(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('sus_exp', sus_exp, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event sus_exp...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_exp.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		sus_exp.__enabled[name] = status


##### -- critic_fail call & handler -- ########################################
class critic_fail(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('critic_fail', critic_fail, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event critic_fail...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(critic_fail.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		critic_fail.__enabled[name] = status


##### -- fail call & handler -- ########################################
class fail(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('fail', fail, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event fail...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(fail.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		fail.__enabled[name] = status


##### -- pos_fail call & handler -- ########################################
class pos_fail(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('pos_fail', pos_fail, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event pos_fail...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(pos_fail.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		pos_fail.__enabled[name] = status


##### -- rst_f call & handler -- ########################################
class rst_f(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_f', rst_f, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_f...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_f.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_f.__enabled[name] = status


##### -- er_gs call & handler -- ########################################
class er_gs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_gs', er_gs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_gs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_gs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_gs.__enabled[name] = status


##### -- gas_found call & handler -- ########################################
class gas_found(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('gas_found', gas_found, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event gas_found...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(gas_found.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		gas_found.__enabled[name] = status


##### -- off_gs call & handler -- ########################################
class off_gs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('off_gs', off_gs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event off_gs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(off_gs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		off_gs.__enabled[name] = status


##### -- on_gs call & handler -- ########################################
class on_gs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('on_gs', on_gs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event on_gs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(on_gs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		on_gs.__enabled[name] = status


##### -- rst_gs call & handler -- ########################################
class rst_gs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_gs', rst_gs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_gs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_gs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_gs.__enabled[name] = status


##### -- move_to call & handler -- ########################################
class move_to(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('move_to', move_to, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event move_to...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(move_to.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		move_to.__enabled[name] = status


##### -- abort_rb call & handler -- ########################################
class abort_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('abort_rb', abort_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event abort_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		abort_rb.__enabled[name] = status


##### -- end_rb call & handler -- ########################################
class end_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('end_rb', end_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event end_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		end_rb.__enabled[name] = status


##### -- er_rb call & handler -- ########################################
class er_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_rb', er_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_rb.__enabled[name] = status


##### -- rsm_rb call & handler -- ########################################
class rsm_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rsm_rb', rsm_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rsm_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rsm_rb.__enabled[name] = status


##### -- rst_rb call & handler -- ########################################
class rst_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_rb', rst_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_rb.__enabled[name] = status


##### -- st_rb call & handler -- ########################################
class st_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('st_rb', st_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event st_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		st_rb.__enabled[name] = status


##### -- sus_rb call & handler -- ########################################
class sus_rb(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('sus_rb', sus_rb, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event sus_rb...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_rb.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		sus_rb.__enabled[name] = status


##### -- end_tele call & handler -- ########################################
class end_tele(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('end_tele', end_tele, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event end_tele...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_tele.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		end_tele.__enabled[name] = status


##### -- er_tele call & handler -- ########################################
class er_tele(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_tele', er_tele, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_tele...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_tele.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_tele.__enabled[name] = status


##### -- rst_tele call & handler -- ########################################
class rst_tele(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_tele', rst_tele, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_tele...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_tele.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_tele.__enabled[name] = status


##### -- st_tele call & handler -- ########################################
class st_tele(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('st_tele', st_tele, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event st_tele...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_tele.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		st_tele.__enabled[name] = status


##### -- abort_vsv call & handler -- ########################################
class abort_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('abort_vsv', abort_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event abort_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(abort_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		abort_vsv.__enabled[name] = status


##### -- end_vsv call & handler -- ########################################
class end_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('end_vsv', end_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event end_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(end_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		end_vsv.__enabled[name] = status


##### -- er_vsv call & handler -- ########################################
class er_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_vsv', er_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_vsv.__enabled[name] = status


##### -- rsm_vsv call & handler -- ########################################
class rsm_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rsm_vsv', rsm_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rsm_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rsm_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rsm_vsv.__enabled[name] = status


##### -- rst_vsv call & handler -- ########################################
class rst_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_vsv', rst_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_vsv.__enabled[name] = status


##### -- st_vsv call & handler -- ########################################
class st_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('st_vsv', st_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event st_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(st_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		st_vsv.__enabled[name] = status


##### -- sus_vsv call & handler -- ########################################
class sus_vsv(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('sus_vsv', sus_vsv, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event sus_vsv...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(sus_vsv.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		sus_vsv.__enabled[name] = status


##### -- er_vs call & handler -- ########################################
class er_vs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('er_vs', er_vs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event er_vs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(er_vs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		er_vs.__enabled[name] = status


##### -- off_vs call & handler -- ########################################
class off_vs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('off_vs', off_vs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event off_vs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(off_vs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		off_vs.__enabled[name] = status


##### -- on_vs call & handler -- ########################################
class on_vs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('on_vs', on_vs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event on_vs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(on_vs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		on_vs.__enabled[name] = status


##### -- rst_vs call & handler -- ########################################
class rst_vs(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('rst_vs', rst_vs, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event rst_vs...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(rst_vs.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		rst_vs.__enabled[name] = status


##### -- victim_found call & handler -- ########################################
class victim_found(object):
	__enabled = {}

	@classmethod
	def call(cls, param = None):
		trigger_event('victim_found', victim_found, param)

	@classmethod
	def handler(cls, param = None):
		#Write code here...
		print('Executing event victim_found...')
		pass

	@classmethod
	def get_status(cls):
		'''
		True: event enabled;
		False: event not allowed.
		'''
		return all(victim_found.__enabled.values())

	@classmethod
	def set_status(cls, name, status):
		victim_found.__enabled[name] = status

