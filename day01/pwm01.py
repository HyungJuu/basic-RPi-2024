# 피에조
import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [262, 294, 330, 349, 392, 440, 494, 524]
#melody = [330, 294, 262, 294, 330, 330, 330]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

# 아날로그 출력을 위한 객체생성(440HZ 출력)
Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		Buzz.start(50) # 50%의 시간을 주면서 동작. duty cycle : 50
		for i in range(0, len(melody)):
			Buzz.ChangeFrequency(melody[i])
			time.sleep(0.3)
		Buzz.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
