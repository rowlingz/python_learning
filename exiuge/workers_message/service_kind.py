# -*- coding:utf-8 -*-

import pandas as pd
from df_to_mysql import df_to_mysql


df = pd.read_excel(r'类别.xlsx', encoding='utf-8')

df['类目2'] = df['类目2'].apply(lambda x: x.split())

s = []

for i in range(len(df)):
    for j in df.iloc[i, 2]:
        s.append([df.iloc[i, 0], df.iloc[i, 1], j])

new_df = pd.DataFrame(s, columns=['主类别', '类目', '详情'])
df_to_mysql(new_df, 'service')

print('end')
print(new_df)
