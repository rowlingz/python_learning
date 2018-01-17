#
import numpy as np
import pandas as pd
from scipy import stats
import timeit


file_name = "C:\python_project\z-500-2.csv"
data = pd.read_csv(file_name)
print(data.head())
n_cols = len(data.columns)
n_rows = len(data.index)
print(data.shape)

print(data.describe())

# labels = data['quality']        # 获取指定列
# data = data.drop(['pH'], axis=1)        # 删除指定列（asix=1 以列为单位）
# print(data.head())



# Count distinct
print(len(data.iloc[:, (n_cols - 1)].unique()))                 # unique() 不重复数
print(data.iloc[:, 0:3].apply(lambda x: len(x.unique())))       # apply（lamba f: ） 多次执行f操作


# special Values
np.sum(data.iloc[:, (n_cols - 1)] == 5)

count_zero = data.iloc[:, 0:3].apply(lambda x: np.sum(x == 0))
print("count_zero --->")
print(count_zero)

# mean Value
miss_set = [np.nan, 999999999, -9999999]
print("before--median")
print(np.mean(data.iloc[:, 0]))
print("after--median")
# print(data.iloc[:, 0:4].apply(lambda x: np.median(x[~np.isin(x, miss_set)])))


# mode value (调用scipy 中stat.mode(),返回(众数[0][0]，频数[1][0])
mode = data.iloc[:, [1, 3]].apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[0][0])

mode_count = data.iloc[:, [1, 3]].apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[1][0])
# mode percentage
mode_perct = mode_count / data.shape[0]


# min / max
min = data.iloc[:, 0:4].apply(lambda x: np.min(x[~np.isin(x, miss_set)]))
max = data.iloc[:, 0:4].apply(lambda x: np.max(x[~np.isin(x, miss_set)]))

# quantile values
quantile = np.percentile(data.iloc[:, 3], (1,25,50,75,99))     # 返回一个数值/列表  只能对单个列执行


# Frequent values
print("Frequent value:------------------")
print(data.iloc[:, 3].value_counts())       # dataframe.value_counts() 返回频数
print(data.iloc[:, 3].value_counts().iloc[0:5])


print('quantile----------------------')
print(quantile)


# miss value
print(data.iloc[:, 0:4].apply(lambda x: np.sum(np.isin(x, miss_set))))


# print("mode" )
# print(mode)
# print(mode_count)
# print(mode_perct)
# print(min)

# 测试时间
start = timeit.default_timer()
print(timeit.default_timer() - start)