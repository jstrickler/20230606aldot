#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_aldot_demo import Ui_ALDOTDemo

class ALDOTDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_ALDOTDemo()
        self.ui.setupUi(self)   # build the interface

        # Connect up menu actions
        # self.ui.actionQuit.triggered.connect(self.close)

        # Connect up buttons.
        self.ui.btn_up.clicked.connect(self._pushed_up)
        self.ui.btn_down.clicked.connect(self._pushed_down)

        self.ui.btn_up.setStyleSheet('QPushButton#btn_up {color: green}')
        self.ui.btn_down.setStyleSheet('QPushButton#btn_down {color: red}')


    def _pushed_up(self):
        self.ui.lineEdit.setText("Going up")

    def _pushed_down(self):
        self.ui.lineEdit.setText("Going down")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ALDOTDemoMain()
    main.show()
    app.exec()


