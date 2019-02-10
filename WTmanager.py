from PyQt5.QtCore import Qt, QDateTime, QTimer
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QInputDialog
from PyQt5.QtWidgets import QMessageBox
import sys
import csv

HEADER = ['Date','Clock In','Clock Out']

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.userName = '홍길동'
        self.nowDateTime = ''
        self.nowDate = ''
        self.fileData = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.change_current_time)
        self.timer.start(1000)

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

        self.set_label_text()
        self.lbName.setAlignment(Qt.AlignCenter)
        self.lbName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbName.setStyleSheet("""
            //border:1px solid #84bbf3;
            color:#ffffff;
            font-size:15px;
            text-align:center;
        """)

        self.btnName.setText("사용자 변경")
        self.btnName.clicked.connect(self.change_user_button)
        self.btnName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.btnIn.setText("출근")
        self.btnIn.clicked.connect(self.file_data_read)
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
        self.btnOut.clicked.connect(self.file_data_write)
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

    def print_csv(self):
        f = open(self.userName+'.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow([1,2,3,4,5])
        wr.writerow([1,2,3,4,44,5])
        f.close()

    def set_label_text(self):
        self.lbName.setText('현재 사용자 : ' + self.userName + ' 님<br>' + self.nowDateTime)

    def change_user_button(self):
        text, ok = QInputDialog.getText(self, '사용자 변경', '변경할 사용자명을 입력하세요')
        if ok:
            self.userName = text
            self.set_label_text()

    def change_current_time(self):
        self.nowDateTime = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.nowDate = str(self.nowDateTime[0:10])
        self.set_label_text()

    def file_data_read(self):
        self.fileData = []

        try:
            f = open(self.userName+'.csv', 'r', encoding='utf-8')
            rdr = csv.reader(f)
            for line in rdr:
                self.fileData.append(line)
            f.close()

            self.fileData = self.fileData[1:]
            print(self.fileData)

        except FileNotFoundError:
            pass

    def file_data_write(self):
        try:
            f = open(self.userName + '.csv', 'w', encoding='utf-8', newline='')
            wr = csv.writer(f)

            wr.writerow(HEADER)
            for line in self.fileData:
                wr.writerow(line)
            f.close()

        except:
            QMessageBox.about(self, "주의", "파일 쓰기 실패")
            app.exec_()


    def in_btn_clicked(self):
        self.file_data_read()

        for line in self.fileData:
            if()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
