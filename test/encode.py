#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 09:30
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : encode.py

from urllib.parse import quote

text = '阿里巴巴'
text = quote(text, 'utf-8')
print(text)
