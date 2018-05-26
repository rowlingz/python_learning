# -*- coding:utf-8 -*-
import pandas as pd
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA


origin_filename = "discdata.xls"
transform_filename = "discdata_transform.xls"

# 数据预处理、属性变换
data = pd.read_excel(origin_filename)
# print(data.head())

new_data = data[data['TARGET_ID'] == 184]

data_group = new_data.groupby('COLLECTTIME')

print(data_group.keys)
print("+++++++++++++++++++++")
# print(data_group.groups)


def attr_trans(group):
    result = pd.Series(index=['SYS_NAME', 'CWXT_DB:184:C:\\', 'CWXT_DB:184:D:\\', 'COLLECTTIME'])
    result['SYS_NAME'] = group['SYS_NAME'].iloc[0]
    result['CWXT_DB:184:C:\\'] = group['VALUE'].iloc[0]
    result['CWXT_DB:184:D:\\'] = group['VALUE'].iloc[1]
    result['COLLECTTIME'] = group['COLLECTTIME'].iloc[0]
    return result


data_attr = data_group.apply(attr_trans)
data_attr.to_excel(transform_filename, index=False)
print(data_attr)
print('end')

# 平稳性检验
data = pd.read_excel(transform_filename, index_col='COLLECTTIME')
train_data = data[:-5]
test_data = data[-5:]
# print(train_data)
# print(test_data)

diff = 0

c_data = train_data['CWXT_DB:184:D:\\']
# print(c_data)
print(c_data.dtypes)

adf = ADF(c_data)
while adf[1] >= 0.05:        # adf[1]为p值， p<0.05,认为是平稳序列
    diff += 1
    adf = ADF(c_data.diff(diff).dropna())

print("CWXT_DB:184:D:\\ 经%s阶差分后归于平稳，p值为%s." % (diff, adf[1]))


# 白噪声检验
[[lb], [p]] = acorr_ljungbox(c_data, lags=1)
if p < 0.05:
    print("原始序列为非白噪声序列， 对应的p值为： %s" % p)
else:
    print("原始序列为白噪声序列， 对应的p值为： %s" % p)

[[lb], [p]] = acorr_ljungbox(c_data.diff(diff).dropna(), lags=1)
if p < 0.05:
    print("%s阶差分序列为非白噪声序列， 对应的p值为： %s" % (diff, p))
else:
    print("%s阶差分序列为白噪声序列， 对应的p值为： %s" % (diff, p))


# acf, pacf图
c_data_diff = c_data.diff().dropna()
plot_acf(c_data_diff).show()
plot_pacf(c_data_diff).show()


# 采用极大似然比方法进行模型的参数估计
pmax = int(len(c_data) / 10)
qmax = int(len(c_data) / 10)
print(pmax, qmax)
bic_matrix = []
for p in range(pmax + 1):
    tmp = []
    for q in range(qmax + 1):
        try:
            arima = ARIMA(c_data, order=(p, 1, q))
            result = arima.fit()
            tmp.append(result.bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)

bic_matrix = pd.DataFrame(bic_matrix)
print(bic_matrix)
p, q = bic_matrix.astype('float64').stack(dropna=True).idxmin()
print("BIC最小的p值和q值为： %s, %s" % (p, q))


# 模型残差序列是否为白噪声
lagnum = 12
arima = ARIMA(c_data, (p, 1, q),).fit()
c_data_predict = arima.predict(typ='levels')
pred_error = (c_data_predict - c_data).dropna()

lb, p = acorr_ljungbox(pred_error, lags=lagnum)
h = (p < 0.05).sum()
if h > 0:
    print("模型ARIMA(0, 1, 1)不符合白噪声检验")
else:
    print("模型ARIMA(0, 1, 1)符合白噪声检验")
