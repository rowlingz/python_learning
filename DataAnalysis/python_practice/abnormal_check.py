# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

catering_sale = 'data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')


print("数据查看==============")
print(data.head())

print("数据描述性统计=================")
data_describe = data.describe()
print(data_describe)
print(data_describe.dtypes)

print("数据计数===============")
total_count = len(data)
print(total_count)


# 判断缺失值个数
deviation_calculation = total_count - data_describe.iloc[0, 0]
if deviation_calculation == 0:
    print("无缺失值")
else:
    print("缺失个数为: " + str(deviation_calculation))

# 绘制图像
plt.figure()
p = data.boxplot()

plt.show()
