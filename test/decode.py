#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 09:28
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : decode.py


from urllib.parse import unquote

text = '%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4'
text = unquote(text, 'utf-8')
print(text)
