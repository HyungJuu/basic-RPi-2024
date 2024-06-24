import RPi.GPIO as GPIO
import time

steps = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

try:
	while True:
		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 1)
		time.sleep(0.01)

		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 1)
		GPIO.output(steps[3], 1)
		time.sleep(0.01)

		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 1)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)


		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 1)
		GPIO.output(steps[2], 1)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)

		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 1)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)

		GPIO.output(steps[0], 1)
		GPIO.output(steps[1], 1)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)

		GPIO.output(steps[0], 1)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)


except KeyboardInterrupt:
	GPIO.cleanup()
