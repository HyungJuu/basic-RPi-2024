from flask import Flask

app = Flask(__name__) # name 이름을 통한 flask 객체 생성

@app.route("/") # 라우팅을 위한 뷰함수 등록
def hello():
	return "Hong kil-dong"

if __name__ == "__main__": # 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다
	app.run(host = "0.0.0.0", port = "10111", debug = True) # 실행을 위한 명령문으로 보면 된다
# 포트 번호를 변경하고 싶으면 port = "10111" 형태로 입력
