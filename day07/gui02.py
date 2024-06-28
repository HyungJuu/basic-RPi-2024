import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

ledPins = [4, 17, 22]
#redled = 4
#greenled = 17
#blueled = 22
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 16, 13, 19, 26, 21, 6] # a ~ f 핀
fndSels = [18, 23, 25, 24] # fnd 선택 핀
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
	GPIO.output(fndSegs, False)
	GPIO.output(fndSels[digit], False)
	for fndSeg in fndDatas[fndData]:
		GPIO.output(fndSeg, True)
	time.sleep(0.005)
	GPIO.output(fndSels[digit], Ture)

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
		self.btn_1.clicked.connect(self.btn1Function)
		self.btn_2.clicked.connect(self.btn2Function)
		self.btn_3.clicked.connect(self.btn3Function)
		self.btn_4.clicked.connect(self.btn4Function)
		# 4digit 7세그먼트 스위치
		self.btn_switch.clicked.connect(self.fndOut)

	# led와 관련된 함수
	def btn1Function(self):
		print("Red LED Button Clicked!")
		GPIO.output(ledPins[0], 0)
		GPIO.output(ledPins[1], 1)
		GPIO.output(ledPins[2], 1)

	def btn2Function(self):
		print("Green LED Button Clicked!")
		GPIO.output(ledPins[0], 1)
		GPIO.output(ledPins[1], 0)
		GPIO.output(ledPins[2], 1)

	def btn3Function(self):
		print("Blue LED Button Clicked!")
		GPIO.output(ledPins[0], 1)
		GPIO.output(ledPins[1], 1)
		GPIO.output(ledPins[2], 0)

	# 스위치
	def fndOut(self):
#		count = 0
		display_count(count)
		time.sleep(0.005)
		count += 1
		if count > 9999:
			count = 0
		time.sleep(0.3)
		self.lcdNum.display(count)


	def btn4Function(self):
		print("Exit")
		GPIO.cleanup()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()


#try:
#	while True:
#		if GPIO.input(switch) == True:
#			count += 1
#			if count > 9999:
#				count = 0
#			time.sleep(0.3)
#		display_count(count)
#		time.sleep(0.003)

#except KeyboardInterrupt:
#	GPIO.cleanup()
