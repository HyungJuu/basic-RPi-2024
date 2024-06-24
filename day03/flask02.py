# 정적 라우팅
from flask import Flask

app = Flask(__name__)

# 192.168.5.3:10011로 접속시 출력됨
@app.route("/")
def hello():
	return "Hello World!!"

# 192.168.5.3:10011/name
@app.route("/name")
def name():
	return "<h1>my name is Kim Geun-Ah</h1>"

# 192.168.5.3:10011/age
@app.route("/age")
def age():
	return "<h1>25 year's old</h1>"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "10011", debug = True)

