# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def generate_data(start_date, end_date):
    df = pd.DataFrame([300 + i * 30 + randrange(50) for i in range(31)], columns=['income'],
                      index=pd.date_range(start_date, end_date, freq='D'))

    return df


data = generate_data('20170601', '20170701')

# 绘制时序图
data.plot()
# plt.legend(prop=myfont)
plt.show()
# 绘制自相关图
plot_acf(data).show()
# 绘制偏自相关图
plot_pacf(data).show()

print(data)


