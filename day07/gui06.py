import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

ledPins = [4, 17, 22]
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 16, 13, 19, 26, 21, 6] # a ~ f 핀
fndSels = [24, 25, 23, 18] # fnd 선택 핀
switch = 12

GPIO.setmode(GPIO.BCM)

# Led 핀 초기화
for ledPin in ledPins:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, 1)

# 7세그먼트 핀 초기화
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def display(digit, fndData):
	for i in range(4):
		GPIO.output(fndSels[i], True)
	for i in range(7):
		GPIO.output(fndSegs[i], fndDatas[fndData] &(1<<i))
	GPIO.output(fndSels[digit], False)
	time.sleep(0.005)
	GPIO.output(fndSels[digit], True)

def display_count(count):
	str_count = str(count).zfill(4)
	zero_skip = True
	for i in range(4):
		digit = int(str_count[i])
		if digit != 0 or not zero_skip:
			display(i, digit)
			zero_skip = False

count = 0

form_class = uic.loadUiType("./gui01.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		# led 관련 이벤트 함수등록
		self.btn_red.clicked.connect(self.btn_Red)
		self.btn_green.clicked.connect(self.btn_Green)
		self.btn_blue.clicked.connect(self.btn_Blue)
		self.btn_off.clicked.connect(self.btn_Off)
		self.btn_exit.clicked.connect(self.btn_Exit)
		# 4digit 7세그먼트 스위치
		self.btn_switch.clicked.connect(self.fndOut)

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateDisplay)
		self.timer.start(10)

		self.switch_timer = QTimer(self)
		self.switch_timer.timeout.connect(self.checkSwitch)
		self.switch_timer.start(100)

	# led와 관련된 함수
	def btn_Red(self):
		print("Red LED Button Clicked!")
		GPIO.output(ledPins[0], 0)
		GPIO.output(ledPins[1], 1)
		GPIO.output(ledPins[2], 1)

	def btn_Green(self):
		print("Green LED Button Clicked!")
		GPIO.output(ledPins[0], 1)
		GPIO.output(ledPins[1], 0)
		GPIO.output(ledPins[2], 1)

	def btn_Blue(self):
		print("Blue LED Button Clicked!")
		GPIO.output(ledPins[0], 1)
		GPIO.output(ledPins[1], 1)
		GPIO.output(ledPins[2], 0)

	def btn_Off(self):
		print("LED OFF")
		GPIO.output(ledPins, 1)

	# gui 상의 스위치
	def fndOut(self):
		global count
		count += 1
		if count > 9999: # 9999를 넘어가면 0으로 초기화
			count = 0
		self.lcdNum.display(count)

	# 스위치 함수
	def checkSwitch(self):
		if GPIO.input(switch) == True: # 스위치를 누르면
			self.fndOut() # 함수호출

	def updateDisplay(self): # 주기적인 갱신으로 카운트 전에는 세그먼트가 꺼지지 않도록
		display_count(count)

	def btn_Exit(self):
		print("Exit")
		GPIO.cleanup()
		sys.exit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	sys.exit(app.exec_())
