import RPi.GPIO as GPIO
import time

switch = 6
red = 21
blue = 20
green = 16

GPIO.setmode(GPIO.BCM)

#GPIO핀 설정
GPIO.setup(switch, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

count = 0
try:
	while True:
		if GPIO.input(switch) == True: # 스위치를 누르면
			print("Pushed")
			count += 1 # 스위치 누를때마다 1씩 누적
			if (count % 3 == 1): # 3으로 나눈 나머지가 1이면
				print("ON : red | OFF : blue, green")
				GPIO.output(red, False) # ON
				GPIO.output(blue, True) # OFF
				GPIO.output(green, True) # OFF
				time.sleep(1)
			elif (count % 3 == 2): # 나머지가 2이면
				print("ON : blue | OFF : red, green")
				GPIO.output(red, True) # OFF
				GPIO.output(blue, False) # ON
				GPIO.output(green, True) # OFF
				time.sleep(1)
			elif (count % 3 == 0): # 나머지가 0이면
				print("ON : green | OFF : red, blue")
				GPIO.output(red, True) # OFF
				GPIO.output(blue, True) # OFF
				GPIO.output(green, False) # ON
				time.sleep(1)

except KeyboardInterrupt: # Ctrl+c로 실행종료
	GPIO.cleanup()
