import sys
from PyQt5.QtWidgets import  *
from PyQt5 import uic

form_class = uic.loadUiType("./btn01.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self): # 생성자
		super().__init__()
		self.setupUi(self)
		# 이벤트 함수 등록
		self.btn_1.clicked.connect(self.btn1Function) # btn_1이라는 버튼을 클릭하면 해당 이벤트함수 실행
		self.btn_2.clicked.connect(self.btn2Function)

	def btn1Function(self):
		print("LED ON Button Clicked!")
	def btn2Function(self):
		print("LED OFF Button Clicked!")
	def slot1(self): # qt 안에서 이벤트함수를 만들어 해당함수명으로 작성 가능
		print("EXIT!!")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
