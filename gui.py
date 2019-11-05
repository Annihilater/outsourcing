#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/27 20:18
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : gui.py
import logging
import sys

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPlainTextEdit
from PyQt5.QtCore import QAbstractTableModel, Qt

from main import main
from parse import parse
from ui.window import Ui_mainWindow


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        self.widget.resize(978, 348)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


# def text_browser_widget():
# #     logTextBox = QTextBrowserLogger((QtWidgets.QDialog, QtWidgets.QTextBrowser))
# #     # You can format what is printed to text box
# #     logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
# #     logging.getLogger().addHandler(logTextBox)
# #     # You can control the logging level
# #     logging.getLogger().setLevel(logging.DEBUG)
# #     return logTextBox.widget


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Ui(Ui_mainWindow):
    def __init__(self, mainWindow):
        self.window_title = '批量网站自动使用站内检索关键词并导出 PDF 工具'
        self.excel = None
        self.pdf_dir = None
        self.result = None
        self.df = None
        self.model = None

        super(Ui, self).__init__()
        super(Ui, self).setupUi(mainWindow)  # 向主窗口上添加控件
        super(Ui, self).retranslateUi(mainWindow)
        mainWindow.setWindowTitle(self.window_title)  # 主窗口添加控件之后设置窗口标题才有效
        self.init_Ui()

        logTextBox = QTextEditLogger(self.plainTextEdit)  # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)  # You can control the logging level

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(logTextBox.widget)
        mainWindow.setLayout(layout)

    def init_Ui(self):
        self.toolButton.clicked.connect(self.open_excel)  # 点击导入按钮
        self.toolButton_2.clicked.connect(self.select_pdf_dir)  # 点击 pdf 路径按钮
        self.toolButton_3.clicked.connect(self.crawl)  # 点击启动按钮
        self.lineEdit.setText(self.excel)

    # 选择 excel
    def open_excel(self):
        print('打开目录')
        self.excel, _ = QFileDialog.getOpenFileName()
        print(self.excel)
        self.show_excel()

    # 在 tableView 里显示 excel
    def show_excel(self):
        self.lineEdit.setText(self.excel)  # 在 lineEdit 空间显示 excel 路径
        self.df = parse(self.excel)
        self.df.replace(np.nan, '', inplace=True)  # 将 DataFrame 中的 NaN 换成空字符
        self.model = pandasModel(self.df)
        self.tableView.setModel(self.model)

    # 选择 pdf 存放的目录
    def select_pdf_dir(self):
        print('打开 PDF 存放的目录')
        self.pdf_dir = QFileDialog.getExistingDirectory()
        print(self.pdf_dir)
        self.lineEdit_2.setText(self.pdf_dir)

    # 开始抓取数据
    def crawl(self):
        print('点击启动')
        # sites = parse_excel(self.df)
        # main(sites)
        # self.textBrowser.append('第1条')
        # self.textBrowser.append('第2条')
        # self.textBrowser.append('第3条')
        # self.textBrowser.append('第4条')
        logging.debug('damn, a bug')
        logging.info('something to remember')
        logging.warning('that\'s not right')
        logging.error('foobar')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
