# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
import time


def visit_web(url):
    """获取网页"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    bf = BeautifulSoup(html, "html.parser")
    return bf


def get_contents(url):
    """获取网站目录url"""
    bf = visit_web(url)

    content_div = bf.find('div', class_='secondLevelWrap borderE6')
    content_kind = content_div.find_all('li')

    content_url = [i.find('a').get('href') for i in content_kind[1: -1]]
    name = [i.string for i in content_kind[1: -1]]

    more_kind = content_kind[-1].find_all('a')
    more_url = [j.get('href') for j in more_kind[1:]]
    more_name = [j.string for j in more_kind[1:]]

    content_url.extend(more_url)
    name.extend(more_name)

    result = {'url': content_url, 'name': name}
    result = pd.DataFrame(result)

    result.to_csv('yiou_content.csv', encoding='utf-8', index=False)


def get_info_every_kind(url):
    """获取每个类别下的文章url"""
    bf = visit_web(url)
    page_div = bf.find('ul', class_='pagination')

    # 获取页码数 pages
    end_page = page_div.find('a', class_='end')
    if end_page:
        pages = int(end_page.string)
    else:
        num = page_div.find_all('a', class_='num')
        pages = int(num[-1].string)

    result = []
    for page in range(1, pages+1):
        if page == 1:
            page_url = url
        else:
            page_url = url + "?page=" + str(page)

        page_bf = visit_web(page_url)

        text_div = page_bf.find_all('div', class_="text fl")
        text_url = [i.find('a').get('href') for i in text_div]

        # print(text_url)
        result.extend(text_url)
        time.sleep(0.001)

    return result


def get_text(bf, value, label='div'):
    web = bf.find(label, id=value)
    if web:
        return web.get_text()
    else:
        return None


def get_info_every_text(url, kind):
    bf = visit_web(url)

    title = get_text(bf, label='h1', value='post_title')
    source = get_text(bf, value="post_source")
    # pub_time = get_text(bf, value="post_date")
    pub_time = bf.find('div', class_='hidden').get_text()
    brief = get_text(bf, value="post_brief")

    kind_label_box = bf.find('div', class_="article_info_box_right")
    kind_labels_list = [i.string for i in kind_label_box.find_all('a')]
    kind_labels = ';'.join(kind_labels_list)

    label_box = bf.find('div', class_="article_info_box tags")
    labels_list = [i.string for i in label_box.find_all('a')]
    labels = ';'.join(labels_list)

    result = [kind, url, title, source, pub_time, brief, labels, kind_labels]

    return result


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


def get_url(content_filename):
    # 获取所有文章url
    content_url = pd.read_csv(content_filename, encoding='utf-8')
    content_len = len(content_url)
    for i in range(content_len):
        kind, url = content_url.iloc[i, 0], 'https://www.iyiou.com' + content_url.iloc[i, 1]
        result = get_info_every_kind(url)
        df = pd.DataFrame({'kind': [kind] * len(result), 'url': result})
        df.to_csv('yiou_text_url.csv', encoding='utf-8', mode='a', index=False)
        print(i)

    print('end')


# 获取全部信息

def get_all_info(input_filename):
    yiou_text_url = pd.read_csv(input_filename, encoding='utf-8')

    results, error = [], []
    for i in range(len(yiou_text_url)):
        kind, url = yiou_text_url.iloc[i, 0], 'https://www.iyiou.com' + yiou_text_url.iloc[i, 1]
        try:
            result = get_info_every_text(url, kind)
            results.append(result)
        except Exception as e:
            error.append([i, e])
            continue

        if i % 100 == 0:
            print(i)
            df = pd.DataFrame(results)
            df.to_csv('yiou_detail.csv', mode='a', index=False, header=False, encoding='utf-8')
            results = []

    if results is not []:
        df = pd.DataFrame(results)
        df.to_csv('yiou_detail.csv', mode='a', index=False, header=False, encoding='utf-8')

    if error is not []:
        error_df = pd.DataFrame(error)
        error_df.to_csv('yiou_error.csv', encoding='utf-8', index=False, header=False)
    print('end')


url = "https://www.iyiou.com/i/jiazhuang"

# # 获取目录
# get_contents(url)

# # 获取全部文章的url
# get_url('yiou_content.csv')

# 获取全部文章的具体信息
get_all_info('yiou_text_url.csv')
