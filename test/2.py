#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 15:25
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 2.py


def run(kw, dp, result, url):
    for i in range(1, 6):
        print(url)
        _url = url.format(kw=kw, page=i)
        file_name = kw + '-' + dp + '-' + result + '-' + str(i)
        print(_url, file_name)


if __name__ == '__main__':
    kw = '阿里巴巴有限公司'
    dp = '国家----工商'
    result = '站内截图'
    url = 'http://www.chinatax.gov.cn/s?q=1&qt={kw}&pageSize=10&database=all&siteCode=bm29000002&docQt=&page={page}'
    run(kw, dp, result, url)
