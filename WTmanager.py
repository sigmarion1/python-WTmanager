from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy
import sys
from datetime import datetime
import csv


class MyWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.lbName = QLabel()
        self.btnName = QPushButton()
        self.btnIn = QPushButton()
        self.btnOut = QPushButton()

        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayoutT = QHBoxLayout()

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.init_widget()

    def init_widget(self):

        self.setWindowTitle("출퇴근 기록기 v0.1")
        self.setGeometry(800, 200, 100, 100)
        self.setFixedSize(300, 120)

        self.lbName.setText("XXX님의 출근기록<br>"+str(datetime.now().date()))
        self.lbName.setAlignment(Qt.AlignCenter)
        self.lbName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbName.setStyleSheet("""
            //border:1px solid #84bbf3;
            color:#ffffff;
            font-size:15px;
            text-align:center;
        """)

        self.btnName.setText("사용자 변경")
        self.btnName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        '''
        self.btnName.setStyleSheet("""
        QPushButton{
            background-color:#44c767;
            -moz-border-radius:28px;
            -webkit-border-radius:28px;
            border-radius:28px;
            border:1px solid #18ab29;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-family:Arial;
            font-size:17px;
            padding:16px 31px;
            text-decoration:none;
            text-shadow:0px 1px 0px #2f6627;
        }
        QPushButton:hover {
            background-color:#5cbf2a;
        }
        QPushButton:active {
            position:relative;
            top:1px;
        }
                """) '''

        self.btnIn.setText("출근")
        self.btnIn.clicked.connect(self.check_prv_time)
        self.btnIn.setStyleSheet("""
        QPushButton{
            background-color:#44c767;
            -moz-border-radius:28px;
            -webkit-border-radius:28px;
            border-radius:28px;
            border:1px solid #18ab29;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-family:Arial;
            font-size:15px;
            padding:16px 31px;
            text-decoration:none;
            text-shadow:0px 1px 0px #2f6627;
        }
        QPushButton:hover {
            background-color:#5cbf2a;
        }
        QPushButton:active {
            position:relative;
            top:1px;
        }
                """)

        self.btnOut.setText("퇴근")
        self.btnOut.setStyleSheet("""
        QPushButton{
        	background-color:#44c767;
        	-moz-border-radius:28px;
        	-webkit-border-radius:28px;
        	border-radius:28px;
        	border:1px solid #18ab29;
        	display:inline-block;
        	cursor:pointer;
        	color:#ffffff;
        	font-family:Arial;
        	font-size:15px;
        	padding:16px 31px;
        	text-decoration:none;
        	text-shadow:0px 1px 0px #2f6627;
        }
        QPushButton:hover {
        	background-color:#5cbf2a;
        }
        QPushButton:active {
        	position:relative;
        	top:1px;
        }
                """)

        self.hBoxLayoutT.addWidget(self.lbName)
        self.hBoxLayoutT.addWidget(self.btnName)

        self.hBoxLayout.addWidget(self.btnIn)
        self.hBoxLayout.addWidget(self.btnOut)

        self.mainLayout.addLayout(self.hBoxLayoutT)
        self.mainLayout.addLayout(self.hBoxLayout)

    def check_prv_time(self):
            print(str(datetime.now()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
