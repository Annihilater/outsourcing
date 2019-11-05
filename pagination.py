#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 10:20
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : pagination.py
import asyncio
import os

from log.log import Logger
from save_to_pdf import save_to_pdf


async def pagination(dp, url, kw, sst):
    """
    :param dp:部门
    :param url: 搜索地址
    :param kw: 关键字
    :param sst: 搜索结果类型
    :return:
    """
    log = Logger('log/all.log', level='debug')  # 记录日志
    _tasks = []
    pdf_dir = 'data/pdf/'
    img_dir = 'data/img/'

    for i in range(1, 6):  # 需求只要求对结果页面保存 5 页
        _url = url.format(kw=kw, page=i)
        file_name = kw + '-' + dp + '-' + sst + '-' + str(i)

        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)

        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        # 判断文件是否存在，如果存在就不对该网址的关键字进行搜索保存 pdf
        if not os.path.exists('{pdf_dir}{file_name}.pdf'.format(pdf_dir=pdf_dir, file_name=file_name)):
            _tasks.append(save_to_pdf(_url, file_name))
            log.logger.info(' '.join(['', file_name, '添加分页任务']))
        else:
            log.logger.info(' '.join(['', file_name, '文件已存在']))
    await asyncio.gather(*_tasks)


def one_site_one_kw(dp, url, kw, sst):
    asyncio.get_event_loop().run_until_complete(pagination(dp, url, kw, sst))


if __name__ == '__main__':
    kw = '阿里巴巴有限公司'
    sst = '站内截图'

    # 国家工商
    # dp = '国家---工商'
    # url = 'http://39.97.130.35/s?qt={kw}&tab=all&siteCode=bm30000012&page={page}'

    # 国家税务
    dp = '国家---税务'
    url = 'http://www.chinatax.gov.cn/s?q=1&qt={kw}&pageSize=10&database=all&siteCode=bm29000002&docQt=&page={page}'

    one_site_one_kw(dp, url, kw, sst)

    # print(os.path.exists('data/pdf/阿里巴巴有限公司-国家---税务-站内截图-1.pdf'))
