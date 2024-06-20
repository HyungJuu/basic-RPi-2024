import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [262, 294, 330, 349, 392, 440, 494, 524]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
#		Buzz.start(50)
		a = input('키 입력 >> ')
		if a == '1':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[0])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '2':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[1])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '3':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[2])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '4':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[3])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '5':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[4])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '6':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[5])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '7':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[6])
			time.sleep(0.1)
			Buzz.stop()
		elif a == '8':
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[7])
			time.sleep(0.3)
			Buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
