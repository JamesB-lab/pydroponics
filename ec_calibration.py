import sys
import time

from dfrobot.ads1115  import ADS1115, ADS1115_IIC_ADDRESS1, ADS1115_REG_CONFIG_PGA_6_144V
from dfrobot.dfr0300  import DFR0300
from dfrobot.channels import CHANNEL_EC
from dfrobot.ds18b20 import DS18B20

sensor_temperature = DS18B20()

ads1115 = ADS1115(bus_id = 3)
ads1115.set_addr_ADS1115(ADS1115_IIC_ADDRESS1)

sensor_ec = DFR0300(configfile = 'config/ecdata.txt')
sensor_ec.begin()

while True :
	#Read your temperature sensor to execute temperature compensation
	temperature = sensor_temperature.get_temperature()
	#Sets the gain and input voltage range.
	ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
	#Get the Digital Value of Analog of selected channel
	adc_ec = ads1115.read_voltage(CHANNEL_EC)
	print(f"A0: {adc_ec['r']:d} mV ")
	#Calibrate the calibration data
	sensor_ec.calibration(adc_ec['r'],temperature)
	time.sleep(3.0)
