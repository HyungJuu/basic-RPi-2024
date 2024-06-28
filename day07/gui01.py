import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

ledPins = [4, 17, 22]
#redled = 4
#greenled = 17
#blueled = 22
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 16, 13, 19, 26, 21, 6] # a ~ f pin
fndSels = [18, 23, 25, 24] # fnd 선택 pin

GPIO.setmode(GPIO.BCM)

for ledPin in ledPins:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, 1)

for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.outpu(fndSel, 1)



form_class = uic.loadUiType("./gui01.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		# 이벤트 함수등록
		self.btn_1.clicked.connect(self.btn1Function)
		self.btn_2.clicked.connect(self.btn2Function)
		self.btn_3.clicked.connect(self.btn3Function)
		self.btn_4.clicked.connect(self.btn4Function)


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

	def btn4Function(self):
		print("Exit")
		GPIO.cleanup()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()




