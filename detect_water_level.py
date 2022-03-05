import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ec_pin = 36

GPIO.setup(ec_pin, GPIO.IN)

while True:
    ec_voltage = GPIO.input(ec_pin)
    if ec_voltage == GPIO.LOW:
        msg = 'No water!'
    else:
        msg = 'Water detected!'
    print(f'EC voltage = {ec_voltage} [V] -> {msg}')