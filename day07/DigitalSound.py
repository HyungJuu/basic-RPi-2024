import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import RPi.GPIO as GPIO
import time

melody = [262, 294, 330, 349, 392, 440, 494, 524]
melody1 = [277, 311, 370, 415, 466]

form_fourthwindow = uic.loadUiType("./fourthwindow.ui")[0]

class fourthwindow(QDialog, form_fourthwindow):
	def __init__(self, Buzz):
		super(fourthwindow, self).__init__()
		self.setupUi(self)
		self.buzzer = Buzz
		self.show() # 네번째창 열기

		# 메인으로 돌아가는 함수
		self.btn_back.clicked.connect(self.Back)

		# 도 ~ 도까지의 버튼함수
		self.btn_1.clicked.connect(self.btn_Do)
		self.btn_2.clicked.connect(self.btn_Re)
		self.btn_3.clicked.connect(self.btn_Mi)
		self.btn_4.clicked.connect(self.btn_Fa)
		self.btn_5.clicked.connect(self.btn_Sol)
		self.btn_6.clicked.connect(self.btn_La)
		self.btn_7.clicked.connect(self.btn_Ti)
		self.btn_8.clicked.connect(self.btn_do)

		# 반음 버튼함수
		self.btn_9.clicked.connect(self.btn_a)
		self.btn_10.clicked.connect(self.btn_b)
		self.btn_11.clicked.connect(self.btn_c)
		self.btn_12.clicked.connect(self.btn_d)
		self.btn_13.clicked.connect(self.btn_e)


	def Sound(self, note):
		self.buzzer.start(50)
		self.buzzer.change_frequency(note)
		time.sleep(0.1)
		self.buzzer.stop()

	def btn_Do(self):
		self.Sound(melody[0])

	def btn_Re(self):
		self.Sound(melody[1])

	def btn_Mi(self):
		self.Sound(melody[2])

	def btn_Fa(self):
		self.Sound(melody[3])

	def btn_Sol(self):
		self.Sound(melody[4])

	def btn_La(self):
		self.Sound(melody[5])

	def btn_Ti(self):
		self.Sound(melody[6])

	def btn_do(self):
		self.Sound(melody[7])

	# 검은건반 부분
	def btn_a(self):
		self.Sound(melody1[0])

	def btn_b(self):
		self.Sound(melody1[1])

	def btn_c(self):
		self.Sound(melody1[2])

	def btn_d(self):
		self.Sound(melody1[3])

	def btn_e(self):
		self.Sound(melody1[4])

	def Back(self):
		self.close()

	def keyPressEvent(self, event):
		key = event.key()
		if key == Qt.Key_A:
			self.btn_Do()
		elif key == Qt.Key_S:
			self.btn_Re()
		elif key == Qt.Key_D:
			self.btn_Mi()
		elif key == Qt.Key_F:
			self.btn_Fa()
		elif key == Qt.Key_G:
			self.btn_Sol()
		elif key == Qt.Key_H:
			self.btn_La()
		elif key == Qt.Key_J:
			self.btn_Ti()
		elif key == Qt.Key_K:
			self.btn_do()

		elif key == Qt.Key_W:
			self.btn_a()
		elif key == Qt.Key_E:
			self.btn_b()
		elif key == Qt.Key_T:
			self.btn_c()
		elif key == Qt.Key_Y:
			self.btn_d()
		elif key == Qt.Key_U:
			self.btn_e()
		else:
			super().keyPressEvent(event)




