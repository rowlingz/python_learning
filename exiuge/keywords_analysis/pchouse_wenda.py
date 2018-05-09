# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


def visit_web(url):
    """获取网页"""
    response = requests.get(url)
    response.encoding = 'gb2312'
    html = response.text
    bf = BeautifulSoup(html, "html.parser")
    return bf


def get_main_contents(url):
    """获取类别网址"""
    bf = visit_web(url)
    main_nav = bf.find("div", class_="mainNav-wrap")
    main_list = main_nav.find_all('a')

    content_dic = {}
    for i in main_list[1:]:
        content_dic[i.string] = i.get('href')

    for key in content_dic:
        items_bf = visit_web(content_dic[key])

        items_link = items_bf.find('div', class_="items-link")
        items_list = items_link.find_all('a')
        items_url = [i.get('href') for i in items_list]
        items_name = [i.string for i in items_list]

        kind = [key] * len(items_url)
        df = pd.DataFrame([kind, items_name, items_url])

        result_df = df.T

        result_df.to_csv('pchouse_contents.csv', mode='a', index=False, header=False)

        print(key)


def get_question_info(url):
    bf = visit_web(url)

    pchouse_page = bf.find('div', class_="pchouse_page")
    pages = pchouse_page.find_all('a')
    if pages:
        end_page = pages[-2].string
    else:
        end_page = 1

    result_url, result_title, result_time = [], [], []
    for i in range(int(end_page)):
        if i == 0:
            page_url = url
        else:
            page_url = url[:-1] + '_p%s/' % end_page

        page_bf = visit_web(page_url)

        info_div = page_bf.find('div', class_="pannel-mod")

        title_info = info_div.find_all('li', class_="li-1")
        question_url= [i.find('a').get('href') for i in title_info[1:]]
        question_title = [i.find('a').string for i in title_info[1:]]

        pub_times = info_div.find_all('li', class_="li-4")
        pub_time = [i.get_text() for i in pub_times[1:]]

        result_title.extend(question_title)
        result_url.extend(question_url)
        result_time.extend(pub_time)
    result = [result_title, result_url, result_time]
    print(url)
    return result


# get_main_contents("http://wenda.pchouse.com.cn/")

question_url = pd.read_csv('pchouse_contents.csv', header=None)
# print(question_url)

for i in range(82, len(question_url)):
    url = question_url.iloc[i, 2]
    result = get_question_info(url)

    big_kind, small_kind = question_url.iloc[i, 0], question_url.iloc[i, 1]

    lenth = len(result[0])

    current_time = datetime.date.today()
    all_info = [[big_kind] * lenth, [small_kind] * lenth, [current_time] * lenth]
    all_info.extend(result)

    # print(all_info)
    df = pd.DataFrame(all_info)

    result_df = df.T

    result_df.to_csv('pchouse_detail2.csv', mode='a', index=False, header=False)

    print(i)

print('end')

