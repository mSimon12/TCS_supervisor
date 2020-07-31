import pandas as pd

'''
	This file contains all the events (controllable and non-controllable)
	related to the Automata created. Each high-level event has a call method
	that is responsible for executing the event.

	The procedures related to each event must be implemented into the 'handler' method.

	*If desired, the hl_2_ll function can be called into the handler to translate the
	current high-level event to a low-level signal configured on the translation_table.csv
'''

def hl_2_ll(hl_event):
	'''
	This function is responsible for translating high-level events into low-level signals.
	'''
	# Get translation table (high-level -> low-level)
	filename = 'OP/translation_table.csv'
	translation_table = pd.read_csv(filename)
	ll_event = translation_table[(translation_table['high-level']==hl_event)]['low-level'].array	# Translate event
	return ll_event


##### -- bat_L call & handler -- ########################################
class bat_L(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return bat_L.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		bat_L.__enabled[name] = status


##### -- bat_LL call & handler -- ########################################
class bat_LL(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return bat_LL.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		bat_LL.__enabled[name] = status


##### -- bat_OK call & handler -- ########################################
class bat_OK(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return bat_OK.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		bat_OK.__enabled[name] = status


##### -- abort_app call & handler -- ########################################
class abort_app(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return abort_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		abort_app.__enabled[name] = status


##### -- end_app call & handler -- ########################################
class end_app(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return end_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		end_app.__enabled[name] = status


##### -- er_app call & handler -- ########################################
class er_app(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_app.__enabled[name] = status


##### -- rsm_app call & handler -- ########################################
class rsm_app(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rsm_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rsm_app.__enabled[name] = status


##### -- rst_app call & handler -- ########################################
class rst_app(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_app.__enabled[name] = status


##### -- st_app call & handler -- ########################################
class st_app(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return st_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		st_app.__enabled[name] = status


##### -- sus_app call & handler -- ########################################
class sus_app(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return sus_app.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		sus_app.__enabled[name] = status


##### -- abort_exp call & handler -- ########################################
class abort_exp(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return abort_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		abort_exp.__enabled[name] = status


##### -- end_exp call & handler -- ########################################
class end_exp(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return end_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		end_exp.__enabled[name] = status


##### -- er_exp call & handler -- ########################################
class er_exp(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_exp.__enabled[name] = status


##### -- rsm_exp call & handler -- ########################################
class rsm_exp(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rsm_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rsm_exp.__enabled[name] = status


##### -- rst_exp call & handler -- ########################################
class rst_exp(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_exp.__enabled[name] = status


##### -- st_exp call & handler -- ########################################
class st_exp(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return st_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		st_exp.__enabled[name] = status


##### -- sus_exp call & handler -- ########################################
class sus_exp(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return sus_exp.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		sus_exp.__enabled[name] = status


##### -- er_gs call & handler -- ########################################
class er_gs(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_gs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_gs.__enabled[name] = status


##### -- gas_found call & handler -- ########################################
class gas_found(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return gas_found.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		gas_found.__enabled[name] = status


##### -- off_gs call & handler -- ########################################
class off_gs(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return off_gs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		off_gs.__enabled[name] = status


##### -- on_gs call & handler -- ########################################
class on_gs(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return on_gs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		on_gs.__enabled[name] = status


##### -- rst_gs call & handler -- ########################################
class rst_gs(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_gs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_gs.__enabled[name] = status


##### -- abort_rb call & handler -- ########################################
class abort_rb(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return abort_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		abort_rb.__enabled[name] = status


##### -- end_rb call & handler -- ########################################
class end_rb(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return end_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		end_rb.__enabled[name] = status


##### -- er_rb call & handler -- ########################################
class er_rb(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_rb.__enabled[name] = status


##### -- rsm_rb call & handler -- ########################################
class rsm_rb(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rsm_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rsm_rb.__enabled[name] = status


##### -- rst_rb call & handler -- ########################################
class rst_rb(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_rb.__enabled[name] = status


##### -- st_rb call & handler -- ########################################
class st_rb(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return st_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		st_rb.__enabled[name] = status


##### -- sus_rb call & handler -- ########################################
class sus_rb(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return sus_rb.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		sus_rb.__enabled[name] = status


##### -- end_tele call & handler -- ########################################
class end_tele(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return end_tele.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		end_tele.__enabled[name] = status


##### -- er_tele call & handler -- ########################################
class er_tele(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_tele.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_tele.__enabled[name] = status


##### -- rst_tele call & handler -- ########################################
class rst_tele(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_tele.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_tele.__enabled[name] = status


##### -- st_tele call & handler -- ########################################
class st_tele(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return st_tele.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		st_tele.__enabled[name] = status


##### -- abort_vsv call & handler -- ########################################
class abort_vsv(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return abort_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		abort_vsv.__enabled[name] = status


##### -- end_vsv call & handler -- ########################################
class end_vsv(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return end_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		end_vsv.__enabled[name] = status


##### -- er_vsv call & handler -- ########################################
class er_vsv(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_vsv.__enabled[name] = status


##### -- rsm_vsv call & handler -- ########################################
class rsm_vsv(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rsm_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rsm_vsv.__enabled[name] = status


##### -- rst_vsv call & handler -- ########################################
class rst_vsv(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_vsv.__enabled[name] = status


##### -- st_vsv call & handler -- ########################################
class st_vsv(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return st_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		st_vsv.__enabled[name] = status


##### -- sus_vsv call & handler -- ########################################
class sus_vsv(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return sus_vsv.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		sus_vsv.__enabled[name] = status


##### -- er_vs call & handler -- ########################################
class er_vs(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return er_vs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		er_vs.__enabled[name] = status


##### -- off_vs call & handler -- ########################################
class off_vs(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return off_vs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		off_vs.__enabled[name] = status


##### -- on_vs call & handler -- ########################################
class on_vs(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return on_vs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		on_vs.__enabled[name] = status


##### -- rst_vs call & handler -- ########################################
class rst_vs(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return rst_vs.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		rst_vs.__enabled[name] = status


##### -- victim_found call & handler -- ########################################
class victim_found(object):
	__enabled = {}
	__type = 'uncontrollable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return victim_found.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		victim_found.__enabled[name] = status


##### -- move_to call & handler -- ########################################
class move_to(object):
	__enabled = {}
	__type = 'controllable'

	@classmethod
	def handler(cls, param = None):
		##### >>>>>>>>>>>>>>>>>>>>>    WRITE YOUR CODE HERE    <<<<<<<<<<<<<<<<<<<<<<< #####
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
	def is_controllable(cls):
		return move_to.__type == 'controllable'

	@classmethod
	def set_status(cls, name, status):
		move_to.__enabled[name] = status

