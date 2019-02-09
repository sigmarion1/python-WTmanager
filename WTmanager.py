from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QLabel
import sys
from datetime import datetime
import csv


class MyWindow(QWidget):

    def __init__(self):

        super().__init__()

        # declare widget variables
        self.btnIn = QPushButton()
        self.btnOut = QPushButton()
        self.lbName = QLabel()

        self.hBoxLayout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.init_widget()

    def init_menubar(self):
        pass


    def init_widget(self):

        self.setWindowTitle("출퇴근 기록기 v0.1")
        self.setGeometry(800, 200, 100, 100)
#        self.setFixedSize(200, 100)

        self.lbName.setText("XXX님의 출근기록")

        self.btnIn.setText("출근")

        self.btnOut.setText("퇴근")

        self.hBoxLayout.addWidget(self.btnln)
        self.hBoxLayout.addWidget(self.btnOut)

        self.mainLayout.addWidget(self.lbName)
        self.mainLayout.addLayout(self.hBoxLayout)

        check_prv_time()


def check_prv_time():
    print('check')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

    ''''
    
           self.verticalLayoutL = QVBoxLayout(self.leftFrame)
        self.gridLayout = QGridLayout()

        self.gridLayout.setSpacing(20)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(6, 2)

        self.gridLayout.setRowStretch(0,20)
        self.gridLayout.setRowStretch(7,2)

        self.lbArray = list()

        for i in range(6):
            for j in range(5):
                self.lb = QLabel(self)

                self.lb.setText(str(i*5 + j + 1))
                self.lb.setStyleSheet("""
                    background-color: rgba(100, 255, 255, 0);
                    color: white;
                    font : 70px;
                    text-align: center;
                    border: 3px solid burlywood;
                    border-radius: 10px;
                    border-style: inset;
                """)
                self.lb.setFixedWidth(130)
                self.lb.setFixedHeight(70)
                self.lb.setAlignment(Qt.AlignCenter)
                self.lbArray.append(self.lb)
                self.gridLayout.addWidget(self.lb, i+1, j+1)



        self.verticalLayoutL.addLayout(self.gridLayout)
        self.verticalLayoutL.setSpacing(10)
    
    
    '''