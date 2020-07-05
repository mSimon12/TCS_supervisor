from threading import Thread



##### -- BAT_OK call & handler -- ########################################
def BAT_OK(param = None):
	h = Thread(target=BAT_OK_handler, args=[param])
	h.start()

def BAT_OK_handler(param = None):
	#Write code here...
	print('BAT_OK running ...')
	pass


##### -- CRITICAL call & handler -- ########################################
def CRITICAL(param = None):
	h = Thread(target=CRITICAL_handler, args=[param])
	h.start()

def CRITICAL_handler(param = None):
	#Write code here...
	print('CRITICAL running ...')
	pass


##### -- LOW call & handler -- ########################################
def LOW(param = None):
	h = Thread(target=LOW_handler, args=[param])
	h.start()

def LOW_handler(param = None):
	#Write code here...
	print('LOW running ...')
	pass