# 풀이
import RPi.GPIO as GPIO
import time

# 0~9 까지 1byte hex값
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 16, 13, 19, 26, 21, 6] # a ~ f pin
fndSels = [18, 23, 25, 24] # fnd 선택 pin

# GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data, sel): # 하나의 숫자형태를 만드는 함수
#	for h in range(0, 50):
		for i in range(0, 7): # a ~ f 까지 on되는 led를 켠다
			GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i)) # 화살표 방향(좌측)으로 i만큼 이동
			# i = 1 : 0000 0001 -> 0000 0010
			for j in range(0, 4): # 표시할 자리수의 fnd만 on
				if j == sel:
					GPIO.output(fndSels[j], 0)
				else:
					GPIO.output(fndSels[j], 1)

# 0부터 출력하려면 count = -1
count = 9995

try:
	while True:
		count += 1
		d1000 = count / 1000
		d100 = count % 1000 / 100
		d10 = count % 100  / 10
		d1 = count % 10

		d =  [d1, d10 ,d100, d1000]

		for i in range(3, -1, -1): # fnd 선택 for문
			fndOut(int(d[i]), i) # byte 표현함수 호출. 자리수와 값을 전달
			time.sleep(0.1)

		# count가 9999를 넘어가면 overflow 발생
		if count == 9999: # count가 9999가 되면
			count = -1	# count를 -1로 초기화해서 0000부터 다시 출력

except KeyboardInterrupt:
	GPIO.cleanup()
