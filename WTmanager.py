from PyQt5.QtWidgets import *
import sys
import openpyxl

import csv


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("자리배치 프로그램 v1.0")

        self.setGeometry(800, 200, 800, 600)
        self.setFixedSize(1000, 800)


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