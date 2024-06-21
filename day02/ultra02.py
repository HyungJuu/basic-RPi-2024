import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True)
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time()

	while GPIO.input(echoPin) == False:
		start = time.time()

	while GPIO.input(echoPin) == True:
		stop = time.time()
	elapsed = stop - start
	distance = (elapsed * 19000) / 2

	return distance

# 핀 설정
# 적외선센서 핀
trigPin = 27
echoPin = 19
# 피에조부저 핀
piezoPin = 13
# LED 핀
redpin = 21
bluepin = 20
greenpin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		distance = measure()
		# LED를 OFF 상태로 초기화
		GPIO.output(redpin, True)
		GPIO.output(bluepin, True)
		GPIO.output(greenpin, True)
		print("Distance : %.2f cm" %distance)

		if distance > 50:
			GPIO.output(bluepin, False)
			time.sleep(1)

		elif distance <= 50 and distance > 40:
			Buzz.start(50)
			GPIO.output(bluepin, False)
			time.sleep(0.8)
			Buzz.stop()
			GPIO.output(bluepin, True)

		elif distance <= 40 and distance > 30:
			Buzz.start(50)
			GPIO.output(greenpin, False)
			time.sleep(0.6)
			Buzz.stop()
			GPIO.output(greenpin, True)

		elif distance <= 30 and distance > 20:
			Buzz.start(50)
			GPIO.output(greenpin, False)
			time.sleep(0.4)
			Buzz.stop()
			GPIO.output(greenpin, True)

		elif distance <= 20 and distance > 10:
			Buzz.start(50)
			GPIO.output(redpin, False)
			time.sleep(0.2)
			Buzz.stop()
			GPIO.output(redpin, True)

		elif distance <= 10 and distance > 5:
			Buzz.start(50)
			GPIO.output(redpin, False)
			time.sleep(0.1)
			Buzz.stop()
			GPIO.output(redpin, True)

		else:
			Buzz.start(50)
			GPIO.output(redpin, False)
			time.sleep(0.05)
			Buzz.stop()
		time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
