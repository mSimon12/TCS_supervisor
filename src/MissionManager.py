from threading import Thread
import time

from handlers.EVENTS import *

class MissionManager(Thread):

    def __init__(self):
        Thread.__init__(self)   
    
    def run(self):
        # while True:
        # time.sleep(1)
        on_vs.call()

        # time.sleep(1)
        on_gs.call()

        # time.sleep(1)
        st_app.call()

        # time.sleep(1)
        end_app.call()

        # time.sleep(1)
        off_vs.call()

        # time.sleep(1)
        off_gs.call()
    
