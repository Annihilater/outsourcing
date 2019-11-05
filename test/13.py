#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/1 12:18
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : 13.py

import asyncio
import re
import time

from pyppeteer import launch

from log.log import Logger


async def save_to_pdf(url, file, kw):
    """
    将搜索结果页面保存为 pdf
    :param url:搜索地址
    :param file: 要保存的文件名
    :return:
    """

    width, height = 1200, 1800
    browser = await launch(args=[f'--window-size={width},{height}',
                                 '--disable-extensions',
                                 '--hide-scrollbars',
                                 '--disable-bundled-ppapi-flash',
                                 '--mute-audio',
                                 '--no-sandbox',
                                 '--disable-setuid-sandbox',
                                 '--disable-gpu'],
                           dumpio=True,
                           headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    # 修改 window.navigator.webdriver 为 False，用于反爬
    await page.evaluate("""
        () =>{
            Object.defineProperties(navigator,{
                webdriver:{
                get: () => false
                }
            })
        }
    """)

    try:
        await page.goto(url)

        await page.type('#qt', kw)  # 定位 #qt 输入框元素，并向元素输入关键字
        await page.click('.search_btn')  # 定位搜索按钮元素，并点击
        await asyncio.sleep(3)

        img_file_path = 'data/img/{}.png'.format(file)
        pdf_file_path = 'data/pdf/{}.pdf'.format(file)
        await page.screenshot(path=img_file_path)

        # await page.emulateMedia('print')
        # await page.pdf({
        #     'width': '8.27in',
        #     'height': '11.7in',
        #     'path': pdf_file_path,
        #     'displayHeaderFooter': True,
        #     'margin': {
        #         'left': '38.4px',
        #         'top': '32px',
        #         'right': '38.4px',
        #         'bottom': '32px',
        #     }
        # })
        # log.logger.info('保存成功' + ' ----> ' + file + '.pdf')

    except Exception:
        print('失败')
    finally:
        await browser.close()


if __name__ == '__main__':
    kw = '阿里巴巴有限公司'
    sst = '站内截图'

    # dp = '国家---税务'
    # url = 'http://www.chinatax.gov.cn/s?q=1&qt={kw}&pageSize=10&database=all&siteCode=bm29000002&docQt=&page={page}'

    # dp = '国家---劳动'
    # url = 'http://search.mohrss.gov.cn/was5/web/search?channelid=296589&searchword={kw}&searchword={kw}&chnls=have&searchscope=&page={page}'

    # dp = '国家---工商'
    # url = 'http://39.97.130.35/s?qt={kw}&tab=all&siteCode=bm30000012&page={page}'

    url = 'http://www.samr.gov.cn/'
    filename = 'new'
    asyncio.get_event_loop().run_until_complete(save_to_pdf(url, filename, kw))
