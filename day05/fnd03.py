# 숫자 앞의 0을 출력안하도록 한 방법
import RPi.GPIO as GPIO
import time

# 세그먼트 핀 정의
segments = [20, 16, 13, 19, 26, 21, 6]

# 각 숫자에 대응하는 세그먼트 패턴 정의
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

# 숫자에 따른 세그먼트 패턴 리스트
numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# 스위치 및 공통 핀 설정
switch = 12
coms = [24, 23, 25, 18]  # 4자리 공통 음극 핀

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, False) # 실행시 세그먼트 핀이 꺼진상태로 초기화

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 스위치 내부 저항설정
for com in coms:
    GPIO.setup(com, GPIO.OUT)
    GPIO.output(com, True)  # 공통 음극 핀은 꺼진 상태로 초기화

# 숫자 출력 함수
def display(digit, number):
    GPIO.output(segments, False) # 모든 세그먼트 핀 끄기
    # 해당 자리의 공통 음극 핀 켜기 (Low 상태)
    GPIO.output(coms[digit], False) # 해당 자리의 공통 음극 핀 켜기
    # 숫자의 세그먼트 켜기
    for segment in numbers[number]:
        GPIO.output(segment, True)
    time.sleep(0.005)
    # 자리 끄기
    GPIO.output(coms[digit], True)

# 카운트 숫자 출력 함수
def display_count(count):
    str_count = str(count).zfill(4) # 예를들어 1이라는 정수를 0001(문자열)로 변환해준다
    # 카운트한 숫자를 제외한 자리의 0은 출력하지 않고 위치 그대로 출력
    # 변환한 0001에서 000은 출력하지 않고 1만 해당위치 그대로 출력함
    zeros_skip = True
    for i in range(4):
        digit = int(str_count[i]) # str_count의 각 자리를 정수로 변환하여 저장
        # 예를들어 str_count가 0001이면 digit에 0, 0, 0, 1 순서대로 저장
        if digit != 0 or not zeros_skip: # digit가 0이 아니거나 앞자리의 0을 스킵할 필요가 있으면
            display(i, digit) # i번째 자리에 해당 숫자를 표시
            zeros_skip = False  # 맨 앞의 0이 아닌 숫자를 만나면 zeros_skip를 False로 변경

count = 0

try:
    while True:
        if GPIO.input(switch) == True: # 스위치를 누르면
            count += 1 # count를 1씩 증가시키고
            if count > 9999:	# count가 9999 이상이면
                count = 0	# count 를 0으로 초기화한다
            time.sleep(0.3)
        display_count(count)
        time.sleep(0.005)

except KeyboardInterrupt:
    GPIO.cleanup()
