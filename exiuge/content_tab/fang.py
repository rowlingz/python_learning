# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import pymysql


def insert_data_sql(message):
    """将数据插入到MySQL中"""
    coon = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="exiuge",
        port=3306,
        charset="utf8")
    sql_insert = "INSERT INTO fang_1 (kind, link, title, times, num, wordsbox) " \
                 "VALUES (%s, %s, %s, %s, %s, %s)"
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
    response.encoding = 'GBK'
    html = response.text
    bf = BeautifulSoup(html, "html.parser")
    return bf


def get_content(url):
    """按类别爬取主要的网址"""
    bf = visit_web(url)
    ul = bf.find('ul', class_="nav")
    h3_top_list = ul.find_all('li', class_=None)

    contents = []
    for h3_top in h3_top_list[1:]:
        all_h3 = h3_top.find_all('h3')
        top = all_h3[0].find('a').string
        sub_list = all_h3[1:]
        sub_dir = {}
        for sub in sub_list:
            sub_name = sub.find('a').string
            sub_link = sub.find('a').get('href')
            # sub_dir[sub_name] = sub_link
            contents.append([top, sub_name, sub_link])
        # contents[top] = sub_dir

    return contents


def get_url_every_page(input_url, kind):
    """每一类文章 链接及标签的爬取"""
    bf = visit_web(input_url)

    # 获取该类文章的总页数 pages
    page_div = bf.find('div', class_='news-page clearfix')
    page_url = page_div.find_all('li')
    end_page = page_url[-1].find('a').get('href')
    pages = [i for i in end_page.split('/') if i][-1]

    if int(pages) > 50:
        pages = 50

    result, error = [], []
    for i in range(1, int(pages) + 1):
        # page_link  每页的url
        page_link = input_url + str(i) + str('/')
        # print(page_link)
        page_bf = visit_web(page_link)
        try:
            urls = page_bf.find_all('div', class_='list-right')
            for url in urls:
                links = url.find_all('a')
                result_link = links[0].get('href')
                result.append([kind, result_link])
        except Exception:
            error.append(page_link)
            continue

        print(i)
    print(result)
    print('error', error)

    pd.Series(result).to_csv('result.csv', encoding='utf-8', mode='a', index=False)
    pd.Series(error).to_csv('error.csv', encoding='utf-8', mode='a', index=False)
    return result, error


def get_info_every_url(url, kind):
    """获取每篇文章的具体信息  （时间、浏览量、文章标注）"""
    bf = visit_web(url)
    try:
        detail = bf.find('div', class_='essay')
        title = bf.find('h1', class_='essay_title').get_text()
        # print(title)

        time = str(detail.find('span', class_='time').string)
        number = detail.find('span', class_='essay_view').string
        num = re.compile('\d+').search(number).group()
        # print(time, num)

        page = bf.find('div', class_='essay_zw')
        # text = page.find_all('p', style=None)
        # print(text)

        label_div = bf.find('div', class_='wordsBox clearfix')
        labels = label_div.find_all('a')
        label_list = [i.string for i in labels]
        wordsbox = ';'.join(label_list)
        # print(wordsbox)

        result = [kind, url, title, time, num, wordsbox]
        # print(result)
        return result
    except Exception as e:
        print(e)
        raise e


# url = pd.read_csv('contents.csv', encoding='utf-8')
#
# for i in range(len(url)-1, len(url)):
#     get_url_every_page(url.iloc[i, 3], int(url.iloc[i, 0]))
#     print(url.iloc[i, 3])
#
# # print(url)
# print('end')


df = pd.read_csv('result.csv', encoding='utf-8')


def get_all_info(df):
    """根据全部网页爬取全部信息并存入数据库"""
    results = []
    error = []
    for i in range(len(df)):
        kind, url = df.iloc[i, 0], df.iloc[i, 1]
        try:
            result = get_info_every_url(str(url), int(kind))
            results.append(result)
        except Exception:
            error.append(url)
            continue

        if i % 100 == 0:
            insert_data_sql(results)
            results = []

    if results is not []:
        insert_data_sql(results)

    print('end')
    return error


