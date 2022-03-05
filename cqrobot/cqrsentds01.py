class CQRSENTDS01:
	def __init__(self):
		pass
	
	def read_tds(self, voltage, temperature):
		compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0)
		compensationVoltage = voltage / compensationCoefficient
		tdsValue = (133.42 * compensationVoltage**3 - 255.86 * compensationVoltage**2 + 857.39 * compensationVoltage) * 0.5
		return tdsValue
