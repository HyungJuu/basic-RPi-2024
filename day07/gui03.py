import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

ledPins = [4, 17, 22]
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]  # 0~9까지의 7-segment 데이터
fndSegs = [20, 16, 13, 19, 26, 21, 6]  # a ~ f 핀
fndSels = [18, 23, 25, 24]  # 4자리 선택 핀
switch = 12

GPIO.setmode(GPIO.BCM)

# LED 핀 초기화
for ledPin in ledPins:
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, 1)

# 7-segment 핀 초기화
for fndSeg in fndSegs:
    GPIO.setup(fndSeg, GPIO.OUT)
    GPIO.output(fndSeg, 0)

for fndSel in fndSels:
    GPIO.setup(fndSel, GPIO.OUT)
    GPIO.output(fndSel, 1)

# 스위치 핀 설정
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def display(digit, fndData):
    for i in range(4):
        GPIO.output(fndSels[i], True)
    for i in range(7):
        GPIO.output(fndSegs[i], fndDatas[fndData] & (1 << i))
    GPIO.output(fndSels[digit], False)
    time.sleep(0.005)
    GPIO.output(fndSels[digit], True)

def display_count(count):
    str_count = str(count).zfill(4)
    for i in range(4):
        display(i, int(str_count[i]))

count = 0

form_class = uic.loadUiType("./gui01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.btn1Function)
        self.btn_2.clicked.connect(self.btn2Function)
        self.btn_3.clicked.connect(self.btn3Function)
        self.btn_4.clicked.connect(self.btn4Function)
        self.btn_switch.clicked.connect(self.guiSwitchClicked)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkSwitch)
        self.timer.start(100)

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

    def guiSwitchClicked(self):
        global count
        count += 1
        if count > 9999:
            count = 0
        self.updateDisplay()

    def checkSwitch(self):
        if GPIO.input(switch) == GPIO.HIGH:
            self.guiSwitchClicked()

    def updateDisplay(self):
        display_count(count)
        self.lcdNum.display(count)

    def btn4Function(self):
        print("Exit")
        GPIO.cleanup()
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
