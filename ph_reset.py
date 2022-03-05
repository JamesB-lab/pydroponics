import sys
import time

from dfrobot.sen0161_v2 import SEN0161_V2

ph = SEN0161_V2(configfile = 'config/phdata.txt')
ph.reset()

time.sleep(0.5)
sys.exit(1)
