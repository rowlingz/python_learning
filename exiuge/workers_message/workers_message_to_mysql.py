# -*- coding:utf-8 -*-
import pandas as pd
from df_to_mysql import df_to_mysql


file_name = r'金牌师傅最新2018-4-11.xlsx'

# 获取workers信息（id, 姓名， 电话， 通讯地址 户名  账号	身份证号	收款日期	名额	金额	收款人	是否入库）

data = pd.read_excel(file_name, usecols=[i for i in range(18)], encoding='utf-8', index_col=0)
data = data.drop(['省', '市', '区'], axis=1)
front_data = data[:653]


after_data = pd.read_excel(file_name, usecols=[i for i in range(18)], sheet_name='Sheet3', encoding='utf-8', index_col=0)
after_data = after_data.drop(['省', '市', '区'], axis=1)
print(front_data.tail())
print(after_data.tail())
print(len(front_data))
print(len(after_data))

# new_data = new_data.dropna(how='all')
# new_data.index = [i for i in range(len(new_data))]
# print(len(new_data))


df_to_mysql(front_data, 'workers_message')
df_to_mysql(after_data, 'workers_message')

print('end')
