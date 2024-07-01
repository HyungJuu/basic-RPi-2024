import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time
import datetime

switch = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

form_fifthwindow = uic.loadUiType("./fifthwindow.ui")[0]

class fifthwindow(QDialog, form_fifthwindow):
	def __init__(self):
		super(fifthwindow, self).__init__()
		self.setupUi(self)
		self.show()

		self.btn_back.clicked.connect(self.Back)
		self.btn_pic.clicked.connect(self.Pic)

		self.switch_timer = QTimer(self)
		self.switch_timer.timeout.connect(self.checkSwitch)
		self.switch_timer.start(100)

	# 돌아가기
	def Back(self):
		self.close()

	def Pic(self):
		now = datetime.datetime.now()
		print(now)
		fileName = now.strftime("%Y-%m-%d %H:%M:%S")
		picam2.capture_file(fileName + ".jpg")
		print("Click!")
#	time.sleep(0.2)

	def checkSwitch(self):
		if GPIO.input(switch) == True:
			self.Pic()
