import RPi.GPIO as GPIO
import time

red = 21
blue = 20
green = 16

# GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)
# GPIO핀 설정(입력(IN)/출력(OUT))
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
	while True:
		# 전압차가 있어야 전류가 흐름
		GPIO.output(red, False) # True : 5V, False : 0V
		GPIO.output(blue, True)
		GPIO.output(green, True)
		time.sleep(1)

		GPIO.output(red, True)
		GPIO.output(blue, False)
		GPIO.output(green, True)
		time.sleep(1)

		GPIO.output(red, True)
		GPIO.output(blue, True)
		GPIO.output(green, False)
		time.sleep(1)

except KeyboardInterrupt: # Ctrl + C
	GPIO.cleanup()
