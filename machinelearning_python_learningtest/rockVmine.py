# 从网页上读取统计数据
import urllib.request
import numpy as np
import pylab
import scipy.stats as stats
import sys

# 1. read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

# arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    # split on comma
    row = str(line.strip()).split(',')
    xList.append(row)


print("Number of Rows of Data = " + str(len(xList)))
print("Number of Columns of Data = " + str(len(xList[0])))

# 2. get the character of property
nRows = len(xList)
nColumns = len(xList[1])
colcounts = []                  # 统计整个属性的类型分布情况
for col in range(nColumns):
    types = [0, 0, 0]           # 记录每一个属性的类别统计（数值型-类别型-其他）
    for row in xList:
        try:
            number = float(row[col])
            # if isinstance(number, float):
            types[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                types[1] += 1
            else:
                types[2] += 1
    colcounts.append(types)
# print(colcounts)

# 输出属性分布
print("Col#\tNumber\tString\tother")
col_i = 0
for types in colcounts:
    s = str(col_i) + "\t\t" + str(types[0]) + "\t\t" + str(types[1]) + "\t\t" + str(types[2])
    print(s)
    col_i += 1


# 3.get the summary statistics
# 数值型：统计信息--均值/方差--（以col#3为例）
col = 3
col_data = []
for row in xList:
    col_data.append(float(row[col]))

# 利用NumPy作数值分析
col_array = np.array(col_data)
col_mean = np.mean(col_array)   # 均值
col_sd = np.std(col_array)      # 标准差
print("Col# " + str(col) + "\t\t" + "Mean = " + str(col_mean) +
      "\t\t" + "Standard Deviation = " + str(col_sd))

# 采用百分位数寻找异常值(quartiles, quintiles, deciles)
n_pers = [4, 5, 10]
percen_bdrys = {}
for n_per in n_pers:
    percen_bdry = []
    for i in range(n_per + 1):
        percen_bdry.append(np.percentile(col_array, i * 100 / n_per))
    percen_bdrys[str(n_per)] = percen_bdry
print(percen_bdrys)

# 采用分位数图（Q-Q）确定异常点
stats.probplot(col_data, dist="norm", plot=pylab)
pylab.show()


# 类别型属性--具体类别及数量分布(以col#60为例)
col = 60
col_data = []
for row in xList:
    col_data.append(row[col])
uniques = set(col_data)     # 获取一个无序不重复元素集
lable_count = {}
for unique in uniques:
    lable_count[unique] = 0
for ele in col_data:
    lable_count[ele] += 1

print(lable_count)
