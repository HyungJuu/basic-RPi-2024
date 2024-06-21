import RPi.GPIO as GPIO
import time

pirPin = 24
led = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == True:
			print("detected led on")
			GPIO.output(led, False)
			time.sleep(0.5)
		else:
			GPIO.output(led, True)

except KeyboardInterrupt:
	GPIO.cleanup()
