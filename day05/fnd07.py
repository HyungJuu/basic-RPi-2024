# 숫자 1234 출력
import RPi.GPIO as GPIO
import time

# 세그먼트 핀 설정
segments = [20, 16, 13, 19, 26, 21, 6]

# 숫자별
num0 = [20, 16, 13, 19, 26, 21]
num1 = [16, 13]
num2 = [20, 16, 6, 26, 19]
num3 = [20, 16, 13, 19, 6]
num4 = [16, 13, 21, 6]
num5 = [20, 13, 19, 21, 6]
num6 = [20, 13, 19, 26, 21, 6]
num7 = [20, 16, 13, 21]
num8 = [20, 16, 13, 19, 26, 21, 6]
num9 = [20, 16, 13, 19, 21, 6]

numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# 공통 핀 설정
coms = [24, 23, 25, 18]

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
for segment in segments:
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, False)  # 실행 전에 모든 세그먼트를 꺼줌

for com in coms:
	GPIO.setup(com, GPIO.OUT)
	GPIO.output(com, True)  # 공통 핀을 꺼줌

# 숫자 표시 함수
def display(digit, number):
	# 모든 세그먼트를 꺼줌
	for segment in segments:
		GPIO.output(segment, False)
	# 공통 핀 설정
	for com in coms:
		GPIO.output(com, True)

		# 해당 자릿수의 공통 핀을 켜줌
		GPIO.output(coms[digit], False)

		# 숫자에 해당하는 세그먼트를 켜줌
		for segment in numbers[number]:
			GPIO.output(segment, True)
		time.sleep(0.001)  # 딜레이 추가

		# 해당 자릿수의 공통 핀을 다시 꺼줌
		GPIO.output(coms[digit], True)

# 카운트 숫자를 표시하는 함수
def display_count(count):
	str_count = str(count).zfill(4)  # 4자리로 맞추기

	for i in range(4):
		digit = int(str_count[i])
		display(i, digit)

try:
	while True:
		display_count(1234)  # 1234 표시

except KeyboardInterrupt:
	GPIO.cleanup()
