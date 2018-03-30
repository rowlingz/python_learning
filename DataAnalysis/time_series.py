# -*- coding:utf-8 -*-
# 时间序列学习记录

from datetime import datetime
from datetime import timedelta
# 导入datetime 模块中的datetime对象

import pandas as pd


def datetime_model():
    # 获取当前时间,年 月 日
    now = datetime.now()
    year, month, day = now.year, now.month, now.day

    # 获取dt中date, time
    print(now.date())
    print(now.time())

    # 获取时间序列对象 class 'datetime.datetime'
    timestamp1 = datetime(2018, 1, 2, 12)

    # 两个时间戳间隔得到时间差对象，class 'datetime.timedelta'（days, seconds）
    delta = timestamp1 - datetime(2018, 1, 20)

    # 给datetime对象加上或减去一个或多个timedelta，产生新的对象
    start = timestamp1
    end = start + timedelta(12)


def convert_str_datetime():
    stamp = datetime(2018, 2, 17)

    # dt.strftime(格式)  转换datetime对象格式
    stamp1 = stamp.strftime('%Y-%m-%d')

    # 字符串转换为日期
    stamp2 = datetime.strptime('2011-12-9', '%Y-%m-%d')

    # 借助parse将字符串转换为日期
    from dateutil.parser import parse
    stamp3 = parse('6/1/2009')

    # 借助pandas 处理成组日期
    date_str = ['7/6/2001', '8/9/2010']
    date_time = pd.to_datetime(date_str)

    print(type(date_time))
    print(date_time)
    return stamp


if __name__ == '__main__':
    # convert_str_datetime()
    datetime_model()