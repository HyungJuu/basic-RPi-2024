from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Flask Server Test"

@app.route("/user/<username>")
def name(username):
	return "User : %s" %username

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "10011", debug = True)
