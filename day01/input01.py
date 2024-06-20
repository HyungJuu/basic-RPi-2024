import RPi.GPIO as GPIO
import time

switch = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)

try:
	while True:
		if GPIO.input(switch) == True:
			print("Pushed")
			time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()
