from w1thermsensor import W1ThermSensor

class DS18B20:
	def __init__(self):
		self.sensor = W1ThermSensor()
	
	def get_temperature(self):
		return self.sensor.get_temperature()
