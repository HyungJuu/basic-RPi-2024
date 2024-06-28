import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 16, 13, 19, 26, 21, 6] # a ~ f 핀
fndSels = [24, 25, 23, 18] # fnd 선택 핀
switch = 12

piezoPin = 5
melody = [262, 294, 330, 349, 392, 440, 494, 524]

GPIO.setmode(GPIO.BCM)

# 7세그먼트 핀 초기화
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

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

form_thirdwindow = uic.loadUiType("./thirdwindow.ui")[0]

class thirdwindow(QDialog, form_thirdwindow):
	def __init__(self):
		super(thirdwindow, self).__init__()
		self.setupUi(self)
		self.show() # 세번째창 열기

		self.btn_back.clicked.connect(self.Back)
		# 4digit 7세그먼트 스위치
		self.btn_switch.clicked.connect(self.fndOut)

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateDisplay)
		self.timer.start(10)

		self.switch_timer = QTimer(self)
		self.switch_timer.timeout.connect(self.checkSwitch)
		self.switch_timer.start(100)

	# gui 상의 스위치
	def fndOut(self):
		Buzz.start(50)
		Buzz.ChangeFrequency(melody[4])
		time.sleep(0.1)
		Buzz.stop()
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

	def Back(self):
		self.close() # 창닫기



