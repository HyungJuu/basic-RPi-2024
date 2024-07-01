import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
import ControlLed
import CountNum
import DigitalSound
import PirSensor3

class Buzzer:
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)
		self.buzz = GPIO.PWM(self.pin, 440)

	def start(self, duty_cycle=50):
		self.buzz.start(duty_cycle)

	def change_frequency(self, frequency):
		self.buzz.ChangeFrequency(frequency)

	def stop(self):
		self.buzz.stop()

	def cleanup(self):
		GPIO.cleanup()

piezoPin = 5
Buzz = None

def init_buzzer():
	global Buzz
	if Buzz is None:
		Buzz = Buzzer(piezoPin)


GPIO.setmode(GPIO.BCM)

form_class = uic.loadUiType("./gui03.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		init_buzzer()

		# Control LED 버튼클릭 함수
		self.btn_led.clicked.connect(self.btn_Led)
		# Count Number 버튼클릭 함수
		self.btn_count.clicked.connect(self.btn_Count)
		# Digital Sound 버튼클릭 함수
		self.btn_sound.clicked.connect(self.btn_Sound)
		#
		self.btn_pir.clicked.connect(self.btn_Pir)

		# 프로그램 종료 함수
		self.btn_exit.clicked.connect(self.btn_Exit)

	def btn_Led(self):
		self.hide()
		self.second = ControlLed.secondwindow()
		self.second.exec()
		self.show()

	def btn_Count(self):
		self.hide()
		self.third = CountNum.thirdwindow(Buzz)
		self.third.exec()
		self.show()

	def btn_Sound(self):
		self.hide()
		self.fourth = DigitalSound.fourthwindow(Buzz)
		self.fourth.exec()
		self.show()

	def btn_Pir(self):
		self.hide()
		self.fifth = PirSensor3.fifthwindow()
		self.fifth.exec()
		self.show()

	def btn_Exit(self):
		print("Exit")
		Buzz.cleanup()
		GPIO.cleanup()
		sys.exit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	sys.exit(app.exec_())
