import RPi.GPIO as GPIO
import time

pin = [20, 16, 13, 19, 26, 21, 6]
num1 = [16, 13] # 숫자 1
num2 = [20, 16, 6, 26, 19] # 숫자 2
num3 = [20, 16, 13, 19, 6] # 숫자 3
num4 = [16, 13,  21, 6] # 숫자 4
num5 = [20, 13, 19, 21, 6] # 숫자 5
num6 = [20, 13, 19, 26, 21, 6] # 숫자 6
num7 = [20, 16, 13, 21] # 숫자 7
num8 = [20, 16, 13, 19, 26, 21, 6] # 숫자 8
num9 = [20, 16, 13, 19, 21, 6] # 숫자 9
num0 = [20, 16, 13, 19, 26, 21] # 숫자 0

segment_pin = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(num1, GPIO.OUT)
GPIO.setup(num2, GPIO.OUT)
GPIO.setup(num3, GPIO.OUT)
GPIO.setup(num4, GPIO.OUT)
GPIO.setup(num5, GPIO.OUT)
GPIO.setup(num6, GPIO.OUT)
GPIO.setup(num7, GPIO.OUT)
GPIO.setup(num8, GPIO.OUT)
GPIO.setup(num9, GPIO.OUT)
GPIO.setup(num0, GPIO.OUT)
GPIO.output(pin, False)

try:
	while True:
#		for i in range(0, len(segment_pin)): # 핀순서대로 전원 들어오는것 확인
#			GPIO.output(segment_pin[i], True)
#			time.sleep(1)
#			GPIO.output(segment_pin[i], False)

		for i in range(0, len(segment_pin)):
			GPIO.output(segment_pin[i], True)
			time.sleep(1)
			GPIO.output(segment_pin[i], False)

except KeyboardInterrupt:
	GPIO.cleanup()
