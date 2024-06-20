import RPi.GPIO as GPIO
import time

led = 21

# GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)
# GPIO핀 설정(입력(IN)/출력(OUT))
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		GPIO.output(led, False) # True : 5V, False : 0V

except KeyboardInterrupt: # Ctrl + C
	GPIO.cleanup()
