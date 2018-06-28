# -*- coding:utf-8 -*-

import pandas as pd
import json
from df_to_mysql import df_to_mysql


data = json.load(open('area.json', encoding='utf-8'))


def regroup(data):
    s = []
    for province, citys in data.items():
        for city, county_city in citys.items():
            for county in county_city:
                s.append([province, city, county])

    df = pd.DataFrame(s, columns=['province', 'city', 'county'])
    return df


df = regroup(data)
df_to_mysql(df, 'area')
print("+++++")
