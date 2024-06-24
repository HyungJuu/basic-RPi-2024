# flask03.py의 코드를 수정한 방법
from flask import Flask
import RPi.GPIO as GPIO

led = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

GPIO.output(led, 1)

@app.route("/")
def Hello():
	return "Hello"

@app.route("/led/<state>")
def LED_State(state):
	if state == "on":
		GPIO.output(led, 0)
		return "Blue LED ON!"
	elif state == "off":
		GPIO.output(led, 1)
		return "Blue LED OFF!"
	elif state == "clear":
		GPIO.cleanup()
		return "GPIO Cleanup()"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "11011", debug = True)
