import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rockVmines = pd.read_csv(target_url, header=None, prefix="V")

print(rockVmines.head())
print(rockVmines.tail())

summary = rockVmines.describe()     # 数据集的描述性统计
print(summary)

# 数值型属性的可视化——平行坐标图

for i in range(208):
    if rockVmines.at[i, 'V60'] == "M":
        prcolor = "red"
    else:
        prcolor = "blue"

    dataRow = rockVmines.iloc[i, 0:60]
    dataRow.plot(color=prcolor)
plot.xlabel("Index")
plot.ylabel("Values")
plot.show()

# 属性间的关系可视化——散点图
dataRow2 = rockVmines.iloc[1, 0:60]
dataRow3 = rockVmines.iloc[2, 0:60]
plot.scatter(dataRow2, dataRow3)
plot.xlabel("2nd")
plot.ylabel("3nd")
plot.show()

dataRow21 = rockVmines.iloc[20, 0:60]
plot.scatter(dataRow2, dataRow21)
plot.xlabel("2nd")
plot.ylabel("21st")
plot.show()

# 分类问题标签和属性的相关性
target = []
for i in range(208):
    if rockVmines.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

dataRow35 = rockVmines.iloc[0:208, 35]
plot.scatter(dataRow35, target)
plot.xlabel("35st")
plot.ylabel("Target value")
plot.show()

target2 = []
for i in range(208):
    if rockVmines.iat[i, 60] == "M":
        target2.append(1.0 + uniform(-0.1, 0.1))
    else:
        target2.append(0.0 + uniform(-0.1, 0.1))

plot.scatter(dataRow35, target2, alpha=0.5, s=120)
plot.xlabel("35st")
plot.ylabel("Target2 value")
plot.show()


# 属性对相关性的热图
corMat = DataFrame(rockVmines.corr())
plot.pcolor(corMat)
plot.show()