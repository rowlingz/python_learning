import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot


# 1.get the data
target_url = "https://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/glass/glass.data"

glass_data = pd.read_csv(target_url, header=None, prefix="X")
glass_data.columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']

print(glass_data.head())

# 2.generate statistical summaries
summary = glass_data.describe()
print(summary)


# 3.box plot(排除主键的影响)
n_rows = len(glass_data.index)
n_cols = len(glass_data.columns)

summary2 = glass_data.iloc[:, 1:n_cols].describe()

glass_data_Norm = glass_data.iloc[:, 1:n_cols]
for j in range(n_cols - 1):
    mean = summary2.iloc[1, j]
    std = summary2.iloc[2, j]
    glass_data_Norm.iloc[:, j:(j + 1)] = (glass_data_Norm.iloc[:, j:(j + 1)] - mean) / std
glass_data_array = glass_data_Norm.values
labels = glass_data.columns[1:]
plot.boxplot(glass_data_array, labels=labels)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges_Normalized")
plot.show()


# 平行坐标图
# 属性归一化时考虑所有数值型属性，包括主键
glass_data_Norm2 = glass_data
for j in range(n_cols - 1):
    mean = summary.iloc[1, j]
    std = summary.iloc[2, j]
    glass_data_Norm2.iloc[:, j:(j + 1)] = (glass_data_Norm2.iloc[:, j:(j + 1)] - mean) / std

# 绘图时，排除主键
max_Type = summary.iloc[7, (n_cols - 1)]
for i in range(n_rows):
    datarows = glass_data_Norm2.iloc[i, 1:(n_cols - 1)]
    label_color = glass_data_Norm2.iloc[i, (n_cols - 1)] / max_Type     # 多分类问题，基于（目标值/最大值）选择颜色
    datarows.plot(color=plot.cm.RdYlBu(label_color), alpha=0.5)
plot.xticks(range(9), glass_data.columns[1:10])
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Values_Normalized")
plot.show()

# heat map
corMat = DataFrame(glass_data.iloc[:, 1:(n_cols-1)].corr())
plot.pcolor(corMat)
plot.show()
