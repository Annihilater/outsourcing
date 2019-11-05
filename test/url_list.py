#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 08:34
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : url_list.py
import pandas as pd

path = '../requirements/程序输入输出示例.xlsx'
sheet = pd.read_excel(io=path, sheet_name=1)

url_list = []
for i in range(3, 35):
    item = sheet.iloc[i]
    print(item[5])
    url_list.append(item[5])

print(url_list)
