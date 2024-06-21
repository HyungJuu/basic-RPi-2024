# Ultra
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True) # 10us 동안 high레벨로 trigger를 출력하여 초음파 발생 준비
	time.sleep(0.00001)
	GPIO.output(trigPin, False) # 현재시간 저장
	start = time.time()

	while GPIO.input(echoPin) == False: # echo가 없으면
		start = time.time() # 현재 시간을 start변수에 저장하고

	while GPIO.input(echoPin) == True: # echo가 있으면
		stop = time.time() # 현재 시간을 stop변수에 저장한다
	elapsed = stop - start # 걸린 시간을 구하고
	distance = (elapsed * 19000) / 2 #초음파 속도를 이용해서 거리계산

	return distance # 거리 반환

# 핀 설정
trigPin = 27
echoPin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" %distance)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
