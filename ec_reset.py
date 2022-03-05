import sys
import time

from dfrobot.dfr0300 import DFR0300

sensor_ec = DFR0300(configfile = 'config/ecdata.txt')
sensor_ec.reset()

time.sleep(0.5)
sys.exit(1)
