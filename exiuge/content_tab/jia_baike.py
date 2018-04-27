# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql


web_url = 'http://www.jia.com/baike/'


def insert_data_table(message):
    """将数据插入到MySQL中"""
    coon = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="exiuge",
        port=3306,
        charset="utf8")
    sql_insert = "INSERT INTO qijia (kind, title, link, title_time, see_time) " \
                 "VALUES (%s, %s, %s, %s, %s)"
    cur = coon.cursor()
    try:
        cur.executemany(sql_insert, message)
        coon.commit()
    except Exception as e:
        # print('e')
        raise e
    finally:
        cur.close()
        coon.close()


def visit_web(url):
    """获取网页"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    bf = BeautifulSoup(html, "html.parser")
    return bf


def get_url(url):
    """获取分类网址"""
    bf = visit_web(url)
    kinds = bf.find_all('li', class_='oneNav current')
    results = []
    for kind in kinds:
        titles = kind.find_all('a')
        result = [[titles[0].string, i.string, i.get('href')] for i in titles[1:]]
        results.extend(result)
    print(results)
    df = pd.DataFrame(results)
    df.to_csv('links_qijia.csv', encoding='utf-8')
    print('end')


def get_info_every_kind(url, kind):
    """获取每类的具体的信息"""
    bf = visit_web(url)

    pages = bf.find('div', class_='p_page')

    if len(pages) != 0:
        end_page = pages.find_all('a')[-2].string
    else:
        end_page = 0

    for i in range(int(end_page) + 1):
        if i == 0:
            page_url = url
        else:
            page_url = url + 'p' + str(i) + '/'

        results = []

        # 获取每页的信息
        page_bf = visit_web(page_url)
        details = page_bf.find_all('div', class_='news_matter_detials')
        for detail in details:

            title = detail.find('a').string
            link = detail.find('a').get('href')
            time_detail = detail.find_all('span')
            title_time, see_time = time_detail[0].get_text(), time_detail[1].get_text()

            result = (kind, title, link, title_time, see_time)
            results.append(result)

        insert_data_table(results)
    print(i, 'end')


df = pd.read_csv('links_qijia.csv', encoding='utf-8')

for i in range(len(df)):
    url = 'http://www.jia.com' + str(df.iloc[i, 3])
    get_info_every_kind(url, i)
    print('kind %s end' % i)
print(df)



