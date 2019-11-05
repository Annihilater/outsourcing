#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/26 17:33
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : parse.py

import pandas as pd
import numpy as np

from config import EXCEL_TITLE, NEW_COL


def load_excel(path):
    """
    载入 excel
    :param path:excel 路径
    :return: DataFrame
    """
    df = pd.read_excel(io=path)
    df.columns = EXCEL_TITLE
    df = df.drop([0, 1, 2])  # 删除 excel 前三行，前三行是脏数据
    df = df.reset_index(drop=True)  # 删除行或列之后，索引是不变的，需要重置索引
    return df


def parse(path):
    """
    解析 excel
    :param path:excel 路径
    :return: DataFrame 列表，一个关键字一个 DataFrame
    """
    df = load_excel(path)
    df.replace(np.nan, '', inplace=True)  # 将 DataFrame 中的 NaN 换成空字符

    new_df = df.drop(['国家', '省', '市', '区'], axis=1)  # 删除前 4 列，国家、省、市、区，删除列：axis=1，删除行：axis=0
    for i in range(len(df)):
        row = df.iloc[i]
        name = '-'.join([str(row['省']), str(row['市']), str(row['部门'])])
        if row['国家']:
            name = '-'.join([row['国家'], name])
        new_df.iloc[i]['部门'] = name

    kw1_df = new_df[new_df.关键字1.isin(['阿里巴巴有限公司'])].drop(['关键字2', '搜索结果2', '关键字3', '搜索结果3'], axis=1)
    kw2_df = new_df[new_df.关键字2.isin(['腾讯有限公司'])].drop(['关键字1', '搜索结果1', '关键字3', '搜索结果3'], axis=1)
    kw3_df = new_df[new_df.关键字3.isin(['百度有限公司'])].drop(['关键字1', '搜索结果1', '关键字2', '搜索结果2'], axis=1)
    kw1_df.columns = NEW_COL
    kw2_df.columns = NEW_COL
    kw3_df.columns = NEW_COL
    return [kw1_df, kw2_df, kw3_df]


if __name__ == '__main__':
    path = 'requirements/程序输入输出示例自定的副本.xlsx'
    for df in parse(path):
        print(df)
