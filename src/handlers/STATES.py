from threading import Thread


class approach:

	##### -- AP_ERROR call & handler -- ########################################
	def AP_ERROR(param = None):
		h = Thread(target=approach.AP_ERROR_handler, args=[param])
		h.start()

	def AP_ERROR_handler(param = None):
		#Write code here...
		print('State AP_ERROR running ...')
		pass

	##### -- AP_EXE call & handler -- ########################################
	def AP_EXE(param = None):
		h = Thread(target=approach.AP_EXE_handler, args=[param])
		h.start()

	def AP_EXE_handler(param = None):
		#Write code here...
		print('State AP_EXE running ...')
		pass

	##### -- AP_IDLE call & handler -- ########################################
	def AP_IDLE(param = None):
		h = Thread(target=approach.AP_IDLE_handler, args=[param])
		h.start()

	def AP_IDLE_handler(param = None):
		#Write code here...
		print('State AP_IDLE running ...')
		pass

	##### -- AP_SUSP call & handler -- ########################################
	def AP_SUSP(param = None):
		h = Thread(target=approach.AP_SUSP_handler, args=[param])
		h.start()

	def AP_SUSP_handler(param = None):
		#Write code here...
		print('State AP_SUSP running ...')
		pass

class battery_monitor:

	##### -- BAT_OK call & handler -- ########################################
	def BAT_OK(param = None):
		h = Thread(target=battery_monitor.BAT_OK_handler, args=[param])
		h.start()

	def BAT_OK_handler(param = None):
		#Write code here...
		print('State BAT_OK running ...')
		pass

	##### -- CRITICAL call & handler -- ########################################
	def CRITICAL(param = None):
		h = Thread(target=battery_monitor.CRITICAL_handler, args=[param])
		h.start()

	def CRITICAL_handler(param = None):
		#Write code here...
		print('State CRITICAL running ...')
		pass

	##### -- LOW call & handler -- ########################################
	def LOW(param = None):
		h = Thread(target=battery_monitor.LOW_handler, args=[param])
		h.start()

	def LOW_handler(param = None):
		#Write code here...
		print('State LOW running ...')
		pass

class communication:

	##### -- COMMUNICATION call & handler -- ########################################
	def COMMUNICATION(param = None):
		h = Thread(target=communication.COMMUNICATION_handler, args=[param])
		h.start()

	def COMMUNICATION_handler(param = None):
		#Write code here...
		print('State COMMUNICATION running ...')
		pass

class explore:

	##### -- EXP_ERROR call & handler -- ########################################
	def EXP_ERROR(param = None):
		h = Thread(target=explore.EXP_ERROR_handler, args=[param])
		h.start()

	def EXP_ERROR_handler(param = None):
		#Write code here...
		print('State EXP_ERROR running ...')
		pass

	##### -- EXP_EXE call & handler -- ########################################
	def EXP_EXE(param = None):
		h = Thread(target=explore.EXP_EXE_handler, args=[param])
		h.start()

	def EXP_EXE_handler(param = None):
		#Write code here...
		print('State EXP_EXE running ...')
		pass

	##### -- EXP_IDLE call & handler -- ########################################
	def EXP_IDLE(param = None):
		h = Thread(target=explore.EXP_IDLE_handler, args=[param])
		h.start()

	def EXP_IDLE_handler(param = None):
		#Write code here...
		print('State EXP_IDLE running ...')
		pass

	##### -- EXP_SUSP call & handler -- ########################################
	def EXP_SUSP(param = None):
		h = Thread(target=explore.EXP_SUSP_handler, args=[param])
		h.start()

	def EXP_SUSP_handler(param = None):
		#Write code here...
		print('State EXP_SUSP running ...')
		pass

class failures:

	##### -- CRITIC_F call & handler -- ########################################
	def CRITIC_F(param = None):
		h = Thread(target=failures.CRITIC_F_handler, args=[param])
		h.start()

	def CRITIC_F_handler(param = None):
		#Write code here...
		print('State CRITIC_F running ...')
		pass

	##### -- NO_FAIL call & handler -- ########################################
	def NO_FAIL(param = None):
		h = Thread(target=failures.NO_FAIL_handler, args=[param])
		h.start()

	def NO_FAIL_handler(param = None):
		#Write code here...
		print('State NO_FAIL running ...')
		pass

	##### -- POS_F call & handler -- ########################################
	def POS_F(param = None):
		h = Thread(target=failures.POS_F_handler, args=[param])
		h.start()

	def POS_F_handler(param = None):
		#Write code here...
		print('State POS_F running ...')
		pass

	##### -- SIMP_F call & handler -- ########################################
	def SIMP_F(param = None):
		h = Thread(target=failures.SIMP_F_handler, args=[param])
		h.start()

	def SIMP_F_handler(param = None):
		#Write code here...
		print('State SIMP_F running ...')
		pass

class gas_sensor:

	##### -- GS_ERROR call & handler -- ########################################
	def GS_ERROR(param = None):
		h = Thread(target=gas_sensor.GS_ERROR_handler, args=[param])
		h.start()

	def GS_ERROR_handler(param = None):
		#Write code here...
		print('State GS_ERROR running ...')
		pass

	##### -- GS_OFF call & handler -- ########################################
	def GS_OFF(param = None):
		h = Thread(target=gas_sensor.GS_OFF_handler, args=[param])
		h.start()

	def GS_OFF_handler(param = None):
		#Write code here...
		print('State GS_OFF running ...')
		pass

	##### -- GS_ON call & handler -- ########################################
	def GS_ON(param = None):
		h = Thread(target=gas_sensor.GS_ON_handler, args=[param])
		h.start()

	def GS_ON_handler(param = None):
		#Write code here...
		print('State GS_ON running ...')
		pass

class motion_system:

	##### -- STEP_MOTIONS call & handler -- ########################################
	def STEP_MOTIONS(param = None):
		h = Thread(target=motion_system.STEP_MOTIONS_handler, args=[param])
		h.start()

	def STEP_MOTIONS_handler(param = None):
		#Write code here...
		print('State STEP_MOTIONS running ...')
		pass

class return_to_base:

	##### -- RB_ERROR call & handler -- ########################################
	def RB_ERROR(param = None):
		h = Thread(target=return_to_base.RB_ERROR_handler, args=[param])
		h.start()

	def RB_ERROR_handler(param = None):
		#Write code here...
		print('State RB_ERROR running ...')
		pass

	##### -- RB_EXE call & handler -- ########################################
	def RB_EXE(param = None):
		h = Thread(target=return_to_base.RB_EXE_handler, args=[param])
		h.start()

	def RB_EXE_handler(param = None):
		#Write code here...
		print('State RB_EXE running ...')
		pass

	##### -- RB_IDLE call & handler -- ########################################
	def RB_IDLE(param = None):
		h = Thread(target=return_to_base.RB_IDLE_handler, args=[param])
		h.start()

	def RB_IDLE_handler(param = None):
		#Write code here...
		print('State RB_IDLE running ...')
		pass

	##### -- RB_SUSP call & handler -- ########################################
	def RB_SUSP(param = None):
		h = Thread(target=return_to_base.RB_SUSP_handler, args=[param])
		h.start()

	def RB_SUSP_handler(param = None):
		#Write code here...
		print('State RB_SUSP running ...')
		pass

class teleoperation:

	##### -- TELE_ERROR call & handler -- ########################################
	def TELE_ERROR(param = None):
		h = Thread(target=teleoperation.TELE_ERROR_handler, args=[param])
		h.start()

	def TELE_ERROR_handler(param = None):
		#Write code here...
		print('State TELE_ERROR running ...')
		pass

	##### -- TELE_EXE call & handler -- ########################################
	def TELE_EXE(param = None):
		h = Thread(target=teleoperation.TELE_EXE_handler, args=[param])
		h.start()

	def TELE_EXE_handler(param = None):
		#Write code here...
		print('State TELE_EXE running ...')
		pass

	##### -- TELE_IDLE call & handler -- ########################################
	def TELE_IDLE(param = None):
		h = Thread(target=teleoperation.TELE_IDLE_handler, args=[param])
		h.start()

	def TELE_IDLE_handler(param = None):
		#Write code here...
		print('State TELE_IDLE running ...')
		pass

class verify_surroundings:

	##### -- VSV_ERROR call & handler -- ########################################
	def VSV_ERROR(param = None):
		h = Thread(target=verify_surroundings.VSV_ERROR_handler, args=[param])
		h.start()

	def VSV_ERROR_handler(param = None):
		#Write code here...
		print('State VSV_ERROR running ...')
		pass

	##### -- VSV_EXE call & handler -- ########################################
	def VSV_EXE(param = None):
		h = Thread(target=verify_surroundings.VSV_EXE_handler, args=[param])
		h.start()

	def VSV_EXE_handler(param = None):
		#Write code here...
		print('State VSV_EXE running ...')
		pass

	##### -- VSV_IDLE call & handler -- ########################################
	def VSV_IDLE(param = None):
		h = Thread(target=verify_surroundings.VSV_IDLE_handler, args=[param])
		h.start()

	def VSV_IDLE_handler(param = None):
		#Write code here...
		print('State VSV_IDLE running ...')
		pass

	##### -- VSV_SUSP call & handler -- ########################################
	def VSV_SUSP(param = None):
		h = Thread(target=verify_surroundings.VSV_SUSP_handler, args=[param])
		h.start()

	def VSV_SUSP_handler(param = None):
		#Write code here...
		print('State VSV_SUSP running ...')
		pass

class victim_system:

	##### -- VS_ERROR call & handler -- ########################################
	def VS_ERROR(param = None):
		h = Thread(target=victim_system.VS_ERROR_handler, args=[param])
		h.start()

	def VS_ERROR_handler(param = None):
		#Write code here...
		print('State VS_ERROR running ...')
		pass

	##### -- VS_OFF call & handler -- ########################################
	def VS_OFF(param = None):
		h = Thread(target=victim_system.VS_OFF_handler, args=[param])
		h.start()

	def VS_OFF_handler(param = None):
		#Write code here...
		print('State VS_OFF running ...')
		pass

	##### -- VS_ON call & handler -- ########################################
	def VS_ON(param = None):
		h = Thread(target=victim_system.VS_ON_handler, args=[param])
		h.start()

	def VS_ON_handler(param = None):
		#Write code here...
		print('State VS_ON running ...')
		pass