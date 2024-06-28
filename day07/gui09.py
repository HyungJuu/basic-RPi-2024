import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
import secondwindow
import thirdwindow

GPIO.setmode(GPIO.BCM)

form_class = uic.loadUiType("./gui03.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# Control LED 버튼클릭 함수
		self.btn_led.clicked.connect(self.btn_Led)
		# Count Number 버튼클릭 함수
		self.btn_count.clicked.connect(self.btn_Count)
		# 프로그램 종료 함수
		self.btn_exit.clicked.connect(self.btn_Exit)

	def btn_Led(self):
		self.hide()
		self.second = secondwindow.secondwindow()
		self.second.exec()
		self.show()

	def btn_Count(self):
		self.hide()
		self.third = thirdwindow.thirdwindow()
		self.third.exec()
		self.show()

	def btn_Exit(self):
		print("Exit")
		GPIO.cleanup()
		sys.exit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	sys.exit(app.exec_())
