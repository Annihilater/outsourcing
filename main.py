#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 08:17
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : main.py
import time

import numpy as np

from pagination import one_site_one_kw
from log.log import Logger
from parse import parse


def main(path):
    """
    :param path:excel path
    :return:
    """
    log = Logger('log/all.log', level='debug')  # 记录日志

    dfs = parse(path)
    for df in dfs:  # 遍历三组关键字
        for i in range(len(df)):  # 每组关键字，遍历网站
            row = df.iloc[i]  # row 表示一个网站一个关键词
            dp = row.部门  # 部门
            url = row.搜索网址  # 搜索网址
            kw = row.关键字  # 关键字
            sst = row.搜索结果  # 搜索结果类型
            filename = kw + '-' + dp + '-' + sst
            if not url:  # 如果站点搜索网址没有配置，则不对这个网址进行关键字搜索
                # time.sleep(5)
                one_site_one_kw(dp, url, kw, sst)  # 一个关键词一个网址
                log.logger.info(' '.join(['', filename, '添加站点任务']))
            else:
                log.logger.info(' '.join(['', filename, '失败：没有添加搜索地址，请添加！！！']))


if __name__ == '__main__':
    path = 'requirements/程序输入输出示例自定的副本.xlsx'
    main(path)  # 开始执行主程序
