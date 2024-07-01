import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO

ledPins = [4, 17, 22]

# Led 핀 초기화

form_secondwindow = uic.loadUiType("./secondwindow.ui")[0]

class secondwindow(QDialog, form_secondwindow):
	def __init__(self):
		super(secondwindow, self).__init__()
		GPIO.setmode(GPIO.BCM)
		for ledPin in ledPins:
			GPIO.setup(ledPin, GPIO.OUT)
			GPIO.output(ledPin, 1)

		self.setupUi(self)
		self.show() # 두번째창 열기

		# led 관련 이벤트 함수등록
		self.btn_red.clicked.connect(self.btn_Red)
		self.btn_green.clicked.connect(self.btn_Green)
		self.btn_blue.clicked.connect(self.btn_Blue)
		self.btn_off.clicked.connect(self.btn_Off)

		self.btn_back.clicked.connect(self.Back)

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

	def Back(self):
		GPIO.cleanup(ledPins)
		self.close() # 창닫기
