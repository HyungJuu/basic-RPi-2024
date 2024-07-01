import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time
import datetime

switch = 12
trigPin = 20
echoPin = 21
leds = [4, 22, 17]

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

for led in leds:
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, 1)

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

		self.distance_timer = QTimer(self)
		self.distance_timer.timeout.connect(self.updateDistance)
		self.distance_timer.start(1000)  # 1초마다 거리 측정 업데이트

	# 돌아가기
	def Back(self):
		self.close()

	def Pic(self):
		now = datetime.datetime.now()
		print(now)
		fileName = now.strftime("%Y-%m-%d %H:%M:%S")
		picam2.capture_file(fileName + ".jpg")
		print("Captured!" + fileName + ".jpg")
		self.Loadimage(fileName + ".jpg")

	def measure_distance(self):
		GPIO.output(trigPin, True)
		time.sleep(0.00001)
		GPIO.output(trigPin, False)
		start = time.time()
		while GPIO.input(echoPin) == False:
			start = time.time()
		while GPIO.input(echoPin) == True:
			stop = time.time()
		elapsed = stop - start
		distance = round(((elapsed * 19000) / 2), 1)
		return distance

	def updateDistance(self):
		distance = self.measure_distance()
		self.lcdNumber.display(distance)

	def checkSwitch(self):
		if GPIO.input(switch) == True:
			self.Pic()

	def Loadimage(self, filepath):
		pixmap = QPixmap(filepath)
		if not pixmap.isNull():
			self.lbl_picture.setPixmap(pixmap.scaledToWidth(600))
		else:
			print(f"Failed to load image from {file_path}")
