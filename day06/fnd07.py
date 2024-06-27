# 풀이
import RPi.GPIO as GPIO
import time

# 0~9 까지 1byte hex값
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 16, 13, 19, 26, 21, 6] # a ~ f pin
fndSels = [24, 23, 25, 18] # fnd 선택 pin

# GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data): # 하나의 숫자형태를 만드는 함수
	for i in range(0, 7):
		GPIO.output(fndSegs[i], 0)
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i)) # 화살표 방향(좌측)으로 i만큼 이동
		# i = 1 : 0000 0001 -> 0000 0010

try:
	while True:
		for i in range(0, 4):
			GPIO.output(fndSels[i], 0) # fnd 선택
#			GPIO.output(16, 1)
#			GPIO.output(13, 1)

			for i in range(0, 10):
				fndOut(5)
				time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
