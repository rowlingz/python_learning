# -*- coding:utf-8 -*-
import pandas as pd


# index指定索引
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s.head())


# columns指定列名
d = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=['a', 'b', 'c'])
print(d.head())
