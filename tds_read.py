import sys
import time

from dfrobot.ads1115   import ADS1115, ADS1115_IIC_ADDRESS1, ADS1115_REG_CONFIG_PGA_6_144V
from cqrobot.cqrsentds01 import CQRSENTDS01
from dfrobot.channels  import CHANNEL_TDS
from dfrobot.ds18b20   import DS18B20

sensor_temperature = DS18B20()

ads1115 = ADS1115(bus_id = 3)
ads1115.set_addr_ADS1115(ADS1115_IIC_ADDRESS1)

sensor_tds = CQRSENTDS01()

while True :
	#Read your temperature sensor to execute temperature compensation
	temperature = sensor_temperature.get_temperature()
	#Sets the gain and input voltage range.
	ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
	#Get the Digital Value of Analog of selected channel
	adc_tds = ads1115.read_voltage(CHANNEL_TDS)
	#Convert voltage to EC with temperature compensation
	tds = sensor_tds.read_tds(adc_tds['r'],temperature)
	print(f'Temperature: {temperature:.1f} C | TDS: {tds:.2f} ppm')
	time.sleep(1.0)
