import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

redled = 4
greenled = 17
blueled = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(redled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)
GPIO.setup(blueled, GPIO.OUT)
GPIO.output(greenled, True)
GPIO.output(redled, True)
GPIO.output(blueled, True)

form_class = uic.loadUiType("./gui01.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		# 이벤트 함수등록
		self.btn_1.clicked.connect(self.btn1Function)
		self.btn_2.clicked.connect(self.btn2Function)
		self.btn_3.clicked.connect(self.btn3Function)


	def btn1Function(self):
		print("Red LED Button Clicked!")
		GPIO.output(redled, False)

	def btn2Function(self):
		print("Green LED Button Clicked!")
		GPIO.output(greenled, False)

	def btn3Function(self):
		print("Blue LED Button Clicked!")
		GPIO.output(blueled, False)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()



#except KeyboardInterrupt:
#	GPIO.cleanup()

