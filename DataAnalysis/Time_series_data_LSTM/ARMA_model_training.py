# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.api import tsa


def generate_data(start_date, end_date):
    df = pd.DataFrame([300 + i * 30 + randrange(50) for i in range(31)], columns=['income'],
                      index=pd.date_range(start_date, end_date, freq='D'))

    return df


data = generate_data('20170601', '20170701')
data['income'] = data['income'].astype('float64')

# 绘制时序图
data.plot()
# plt.legend(prop=myfont)
plt.show()
# 绘制自相关图
plot_acf(data).show()
# 绘制偏自相关图
plot_pacf(data).show()

print(data)


# 差分运算
# 默认1阶差分
data_diff = data.diff()

# 差分后需要排空，
data_diff = data_diff.dropna()

data_diff.plot()
plt.show()

plot_acf(data_diff).show()
plot_pacf(data_diff).show()

print('end')


# 模型训练

arima = ARIMA(data, order=(1, 1, 1))
result = arima.fit(disp=False)
print(result.aic, result.bic, result.hqic)

plt.plot(data_diff)
plt.plot(result.fittedvalues, color='red')
plt.title('ARIMA RSS: %.4f' % sum(result.fittedvalues - data_diff['income']) ** 2)
plt.show()

# ARIMA   Ljung-Box检验 -----模型显著性检验，Prod> 0.05，说明该模型适合样本
resid = result.resid
r, q, p = tsa.acf(resid.values.squeeze(), qstat=True)
print(len(r), len(q), len(p))
test_data = np.c_[range(1, 30), r[1:], q, p]
table = pd.DataFrame(test_data, columns=['lag', 'AC', 'Q', 'Prob(>Q)'])
print(table.set_index('lag'))


# 模型预测
pred = result.predict('20170701', '20170710', typ='levels')
print(pred)
x = pd.date_range('20170601', '20170705')
plt.plot(x[:31], data['income'])
# lenth = len()
plt.plot(pred)
plt.show()
print('end')


