import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from math import exp

# 1.获取数据
target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
wine_data = pd.read_csv(target_url, header=0, sep=";")




# 2.数据查看
print(wine_data.head())


# 3.描述性统计
n_cols = len(wine_data.columns)
n_rows = len(wine_data.index)
summary = wine_data.describe()
print(summary)


# 4.异常点-归一化箱线图
wine_data_Norm = wine_data.iloc[:, 0:n_cols]        # 选用切片生成新的Dataframe，避免更改原始数据
for i in range(n_cols):
    mean = summary.iloc[1, i]
    std = summary.iloc[2, i]
    wine_data_Norm.iloc[:, i:(i + 1)] = (wine_data_Norm.iloc[:, i:(i + 1)] - mean) / std
array_Norm = wine_data_Norm.values
plot.boxplot(array_Norm)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges_Normalized")
plot.show()


# 5. 属性对关系---归一化平行坐标图

# 原始图像
min_quality = summary.iloc[3, (n_cols - 1)]
max_quality = summary.iloc[7, (n_cols - 1)]
for i in range(n_rows):
    data_rows = wine_data.iloc[i, 0: (n_cols - 1)]
    label_color = (wine_data.iloc[i, (n_cols - 1)] - min_quality)/(max_quality - min_quality)
    data_rows.plot(color=plot.cm.RdYlBu(label_color), alpha=0.5)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Values")
plot.show()

# 采用分对数变换后
mean_quality = summary.iloc[1, (n_cols - 1)]
std_quality = summary.iloc[2, (n_cols - 1)]
for i in range(n_rows):
    data_rows = wine_data.iloc[i, 0: (n_cols - 1)]
    norm_target = (wine_data.iloc[i, (n_cols - 1)] - mean_quality) / std_quality
    label_color = 1.0 / (1.0 + exp(-norm_target))
    data_rows.plot(color=plot.cm.RdYlBu(label_color), alpha=0.5)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Values_Normalized")
plot.show()


# 在属性值归一化基础上的平行坐标图
wine_data_Norm = wine_data
for j in range(n_cols):
    mean = summary.iloc[1, j]
    std = summary.iloc[2, j]
    wine_data_Norm.iloc[:, j:(j + 1)] = (wine_data_Norm.iloc[:, j:(j + 1)] - mean) / std

for i in range(n_rows):
    data_rows = wine_data_Norm.iloc[i, 0: (n_cols - 1)]
    norm_target = wine_data_Norm.iloc[i, (n_cols - 1)]      # 归一化后，无需将属性值压缩
    label_color = 1.0 / (1.0 + exp(-norm_target))
    data_rows.plot(color=plot.cm.RdYlBu(label_color), alpha=0.5)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Values_Normalized2")
plot.show()


# # 6.属性与标签的关系--热图
corMat = DataFrame(wine_data.corr())
plot.pcolor(corMat)
plot.show()
