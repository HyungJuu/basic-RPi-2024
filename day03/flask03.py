# URL 접속을 /led/on, /led/off로 접속하면 led를 on / off 하는 웹페이지 만들기
from flask import Flask
import RPi.GPIO as GPIO
import time

bluePin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(bluePin, GPIO.OUT)

app = Flask(__name__)

GPIO.output(bluePin, 1)
# LED에 연결된 VCC로 전원이 들어온다
# 0 -> 전압차로 실행과 동시에 불이 들어옴
# 1 -> 전압차를 없앰(불이 켜지지 않음)

@app.route("/")
def Hello():
	return "Hello"

@app.route("/led/on")
def LED_ON():
	GPIO.output(bluePin, 0)
	return "LED ON"

@app.route("/led/off")
def LED_OFF():
	GPIO.output(bluePin, 1)
	return "LED OFF"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "11011", debug = True)
