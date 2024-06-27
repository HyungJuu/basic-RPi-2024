import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test01.ui")[0] # .ui 파일을 class형태로 변환

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self): # 생성자. 첫번째 인자 : self
		super().__init__() # 부모 클래스 생성자(QWidges)
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv) # 프로그램을 실행시키는 클래스
	myWindow = WindowClass() # WindowClass() 인스턴스 생성
	myWindow.show() # 화면 보여주기
	app.exec_() # 프로그램 실행
