# 从网页上读取统计数据
import urllib.request
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
            if isinstance(number, float):
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