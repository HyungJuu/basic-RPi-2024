import RPi.GPIO as GPIO
import time

# 7세그먼트 핀 설정
segments = [20, 16, 13, 19, 26, 21, 6]

# 각 숫자에 해당하는 핀 설정
num0 = [20, 16, 13, 19, 26, 21]  # 숫자 0
num1 = [16, 13]  # 숫자 1
num2 = [20, 16, 6, 26, 19]  # 숫자 2
num3 = [20, 16, 13, 19, 6]  # 숫자 3
num4 = [16, 13, 21, 6]  # 숫자 4
num5 = [20, 13, 19, 21, 6]  # 숫자 5
num6 = [20, 13, 19, 26, 21, 6]  # 숫자 6
num7 = [20, 16, 13, 21]  # 숫자 7
num8 = [20, 16, 13, 19, 26, 21, 6]  # 숫자 8
num9 = [20, 16, 13, 19, 21, 6]  # 숫자 9

# 각 숫자에 해당하는 리스트를 numbers 리스트에 저장
numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# 4개의 공통 핀 설정
coms = [24, 23, 25, 18]  # 4자리 표시 공통 핀

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# 각 세그먼트 핀 및 공통 핀 초기화
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, False)

for com in coms:
    GPIO.setup(com, GPIO.OUT)
    GPIO.output(com, True)

# 숫자 표시 함수 정의
def display(digit, number):
    GPIO.output(segments, False)  # 모든 세그먼트 핀 비활성화
    GPIO.output(coms[digit], False)  # 해당 자리의 공통 핀 활성화

    for segment in numbers[number]:
        GPIO.output(segment, True)  # 숫자에 해당하는 세그먼트 핀 활성화
    
    time.sleep(0.005)  # 각 숫자가 표시될 시간을 짧게 설정

    GPIO.output(coms[digit], True)  # 해당 자리의 공통 핀 비활성화

# 카운트 표시 함수 정의
def display_count(count):
    str_count = str(count).zfill(4)  # 4자리로 표시하고 앞을 0으로 채움

    for i in range(4):
        digit = int(str_count[i])
        display(i, digit)

# 메인 루프 시작
count = 0

try:
    while True:
        for i in range(9999):
            display_count(count)
            time.sleep(0.5)  # 각 자리의 숫자가 표시될 시간을 길게 설정
            count += 1  # 카운트 증가

            if count > 9999:
                count = 0  # 카운트가 9999를 넘으면 0으로 초기화

except KeyboardInterrupt:
    GPIO.cleanup()  # Ctrl+C로 인터럽트 시 GPIO 정리
