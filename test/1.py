#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 14:02
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 1.py
import re

s = 'http://www.chinatax.gov.cn/s?q=1&qt=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&pageSize=10&database=all&siteCode=bm29000002&docQt=&page=4'
a = re.search('(.*)&page=(\d)', s)
print(a.group(0))
