import RPi.GPIO as GPIO
import time

led = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		a = input('키 입력 >> ')
		if a == 'o':
			GPIO.output(led, False)
		elif a == 'x':
			GPIO.output(led, True)
		else:
			print('잘못된 입력입니다. (ON : o / OFF : x)')

except KeyboardInterrupt:
	GPIO.cleanup()
