import sys
import time

from dfrobot.ds18b20 import DS18B20

sensor_temperature = DS18B20()

while True :
	#Convert voltage to temperature
	temperature = sensor_temperature.get_temperature()
	print(f'Temperature: {temperature:.1f} C')
	time.sleep(1.0)
