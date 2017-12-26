import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from math import exp

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
abalone_data = pd.read_csv(target_url, header=None, prefix="X")
abalone_data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight',
                        'Shucked weight', 'Viscera weight', 'Shell weight',
                        'Rings']

print(abalone_data.head())
print(abalone_data.tail())

summary = abalone_data.describe()
print(summary)

# 寻找异常点---每个实数值属性的box plots
abalone_array = abalone_data.iloc[:, 1:9].values
labels = abalone_data.columns[1:9]
plot.boxplot(abalone_array, labels=labels)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
plot.show()


abalone_array = abalone_data.iloc[:, 1:8].values
labels = abalone_data.columns[1:8]
plot.boxplot(abalone_array, labels=labels)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
plot.show()


# 采用Z-score标准化归一化
abalone_data_Normalized = abalone_data.iloc[:, 1:9]
for i in range(8):
    mean = summary.iloc[1, i]
    std = summary.iloc[2, i]
    abalone_data_Normalized.iloc[:, i: (i + 1)] = (abalone_data_Normalized.iloc[:, i: (i + 1)]
                                                   - mean) / std

array_Nor = abalone_data_Normalized.values
plot.boxplot(array_Nor, labels=abalone_data.columns[1:9])
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges_Normalized")
plot.show()

# 回归问题中类别与属性间的关系--平行坐标图（"Rings"与其他数值型属性间的关系）
minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
n_rows = len(abalone_data.index)

for i in range(n_rows):
    data_rows = abalone_data.iloc[i, 1:8]
    label_color = (abalone_data.iloc[i, 8] - minRings) / (maxRings - minRings)
    data_rows.plot(color=plot.cm.RdYlBu(label_color), alpha=0.5)
plot.xticks(range(7), abalone_data.columns[1:8])
plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()

# 平行坐标图归一化
meanRings = summary.iloc[1, 7]
stdRings = summary.iloc[2, 7]
for i in range(n_rows):
    data_rows = abalone_data.iloc[i, 1:8]
    Norm_target = (abalone_data.iloc[i, 8] - meanRings) / stdRings
    label_color = 1.0/(1.0 + exp(-Norm_target))
    data_rows.plot(color=plot.cm.RdYlBu(label_color), alpha=0.5)
plot.xticks(range(7), abalone_data.columns[1:8])
plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values_Normalized")
plot.show()

# 属性对的关联热图
corMat =DataFrame(abalone_data.iloc[:, 1:9].corr())
plot.pcolor(corMat)
plot.show()
