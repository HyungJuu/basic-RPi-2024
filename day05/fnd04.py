# 스위치로 9999까지 카운트(1 -> 0001로 출력됨)
import RPi.GPIO as GPIO
import time

# 핀 번호 정의
segments = [20, 16, 13, 19, 26, 21, 6]
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

# 숫자 배열 설정
numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# 스위치 및 공통 핀 설정
switch = 12
coms = [24, 23, 25, 18]

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, False)

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for com in coms:
    GPIO.setup(com, GPIO.OUT)
    GPIO.output(com, True)  # 공통 음극 핀은 True로 설정하여 꺼진 상태로 초기화

def display(digit, number):
    # 모든 세그먼트를 끄기
    GPIO.output(segments, False)
    # 해당 자리의 공통 음극 핀을 켜기 (Low 상태)
    GPIO.output(coms[digit], False)
    # 숫자의 세그먼트를 켜기
    for segment in numbers[number]:
        GPIO.output(segment, True)
    time.sleep(0.005)
    # 자리 끄기
    GPIO.output(coms[digit], True)

def display_count(count):
    str_count = str(count).zfill(4)
    for i in range(4):
        digit = int(str_count[i])
        display(i, digit)

count = 0
try:
    while True:
        if GPIO.input(switch) == True:
            count += 1
            if count > 9999:
                count = 0
            time.sleep(0.3)
        display_count(count)
        time.sleep(0.005)

except KeyboardInterrupt:
    GPIO.cleanup()
