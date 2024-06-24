from flask import Flask

app = Flask(__name__) # name 이름을 통한 flask 객체 생성

@app.route("/") # 라우팅을 위한 뷰함수 등록
def hello():
	return "Hello World"

if __name__ == "__main__": # 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다
	app.run(host = "0.0.0.0", debug = True) # 실행을 위한 명령문으로 보면 된다
