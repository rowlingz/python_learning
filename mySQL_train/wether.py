# coding = UTF-8

import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd
import numpy
import matplotlib.pyplot as plt

# 杭州--"101210101.shtml"


def get_wether_7th(city):
    url = "http://www.weather.com.cn/weather" + "/" + city
    resp = requests.get(url)
    html = resp.text.encode(resp.encoding).decode('utf-8')
    bf = BeautifulSoup(html, "html.parser")
    infor = bf.find('div', id='7d')
    ul = infor.find('ul')
    li = ul.find_all('li')

    weather_7th = []
    for day in li:
        temp = {}
        date = day.find('h1').string
        if len(date) < 7:
            temp['date'] = date[:2]
        else:
            temp['date'] = date[:3]

        temperature = day.find_all('p')
        temp['weather'] = temperature[0].string

        if temperature[1].find('span') is None:
            temperature_high = 'None'
        else:
            temperature_high = temperature[1].find('span').string.replace('℃', '')
        temp['tem_high'] = temperature_high

        temperature_low = temperature[1].find('i').string
        temp['tem_low'] = temperature_low.replace('℃', '')

        temp['win'] = temperature[2].find('i').string

        weather_7th.append(temp)

    return weather_7th


def insert_weather_table(data):
    coon = pymysql.connect(host="localhost", user="root", password="root", database="njust", port=3306, charset="utf8")
    sql_select = "SELECT * FROM weather WHERE date = %s"
    sql_insert = "INSERT INTO weather VALUES (%s, %s, %s, %s, %s)"
    sql_update = "UPDATE weather SET weather = %s, tem_high = %s, tem_low = %s, win = %s WHERE date = %s"

    for day in data:
        cur = coon.cursor()
        values = (day['date'], day['weather'], day['tem_high'], day['tem_low'], day['win'])
        cur.execute(sql_select, values[0])
        if cur.rowcount != 0:
            new_values = (day['weather'], day['tem_high'], day['tem_low'], day['win'], day['date'])
            cur.execute(sql_update, new_values)
        else:
            cur.execute(sql_insert, values)
        coon.commit()
        cur.close()

    coon.close()


def analysis(table):
    conn = pymysql.connect(host="localhost", user="root", password="root", database="njust", port=3306, charset="utf8")
    sql_select = "SELECT date, tem_high, tem_low FROM " + table
    df = pd.read_sql(sql_select, conn)
    conn.close()
    n_rows = len(df.index)

    x = range(1, n_rows + 1)
    plt.plot(x, df.iloc[:, 2], 'b-o', label='tem_lower')
    plt.plot(x, df.iloc[:, 1], 'r-*', label='tem_higher')

    plt.legend(loc='upper right')

    for a, b in zip(x, df.iloc[:, 2]):
        plt.text(a, int(b), str(b)+"℃",  ha='center', va='bottom')

    for a, b in zip(x, df.iloc[:, 1]):
        plt.text(a, int(b), str(b)+"℃",  ha='center', va='bottom')

    plt.show()

    return df


city = "101210101.shtml"

# data = get_wether_7th(city)
# insert_weather_table(data)


df = analysis('weather')
print(df)
print(type(df.iloc[1, 1]))
if df.iloc[0, 1]:
    print(1)
else:
    print(2)

