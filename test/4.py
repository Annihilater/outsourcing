#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/28 10:46
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 4.py

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

path = '../requirements/程序输入输出示例自定的副本.xlsx'
sheet_num = 2
df = pd.read_excel(io=path, sheet_name=2)


# df = pd.DataFrame({'a': ['Mary', 'Jim', 'John'],
#                    'b': [100, 200, 300],
#                    'c': ['a', 'b', 'c']})


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = pandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec_())
