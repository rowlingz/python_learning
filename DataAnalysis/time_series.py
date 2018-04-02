# -*- coding:utf-8 -*-
# 时间序列学习记录

from datetime import datetime
from datetime import timedelta
# 导入datetime 模块中的datetime对象

import pandas as pd
import numpy as np


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

    # 借助pandas 处理成组的日期, 得到DatetimeIndex
    date_str = ['7/6/2001', '8/9/2010']
    date_time = pd.to_datetime(date_str)

    print(type(date_time))
    print(date_time)
    return stamp


def cut_timeseries():
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
             datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

    ts = pd.Series(np.random.randn(6), index=dates)
    print(ts)
    print(ts['1/10/2011'])
    print(type(ts.index[0]))
    # Series序列日期切片
    print(ts[datetime(2011, 1, 8):])

    long_ts = pd.DataFrame(np.random.randn(4, 4),
                           index=pd.date_range('1/1/2000', periods=4),
                           columns=['a', 'b', 'c', 'd'])
    # print(long_ts)
    # print("+++++")
    # print(long_ts['2001-02'])
    print(long_ts.ix['2000-01-01'])


def rept_time():
    """重复时间处理  groupby(level=0)"""
    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
    ts = pd.Series(np.random.randn(5), index=dates)
    print(ts)
    # print(ts['1/2/2000'])
    # print(ts['1/3/2000'])
    print(ts.index.is_unique)

    # 时间戳聚合，level=0，在索引层分组
    grouped = ts.groupby(level=0)
    print(grouped.mean())
    print(grouped.count())


if __name__ == '__main__':
    # convert_str_datetime()
    rept_time()