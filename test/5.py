#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/28 11:43
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 5.py


import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextBrowser, QPushButton, QWidget, QHBoxLayout
import time
import random


class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self, message):
        # time.sleep(random.random() * 5)
        self.trigger.emit(message)


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.text_area = QTextBrowser()
        self.thread_button = QPushButton('Start threads')
        self.thread_button.clicked.connect(self.start_threads)

        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_layout.addWidget(self.text_area)
        central_layout.addWidget(self.thread_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.threads = MyThread(self)
        self.threads.trigger.connect(self.update_text)

        self.thread_no = 0

    def start_threads(self):
        self.thread_no += 1
        message = "cnt:{0}".format(self.thread_no)
        self.threads.run_(message)  # start the thread
        print(message)

    def update_text(self, message):
        # self.text_area.append('thread # %d finished'%thread_no)
        # print('thread # %d finished'%thread_no)

        self.text_area.append(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = Main()
    mainWindow.show()

    sys.exit(app.exec_())
