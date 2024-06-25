# 동일한 폴더 위치에 templates 폴더를 만들고 거기에 html 파일을 저장한다

from flask import Flask, request, render_template
import RPi.GPIO as GPIO
#from gpiozero import LED

app = Flask(__name__)

bluePin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(bluePin, GPIO.OUT)

GPIO.output(bluePin, True)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/data", methods = ["POST"])
def data():
	data = request.form["led"]

	if data == "on":
		GPIO.output(bluePin, False)
		return home()

	elif data == "off":
		GPIO.output(bluePin, True)
		return home()

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "11011", debug = True)
