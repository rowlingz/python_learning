# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


def visit_web(url):
    """获取网页"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    bf = BeautifulSoup(html, "html.parser")
    return bf


def get_big_kind_url(url):
    """获取类别链接"""
    bf = visit_web(url)

    contents = bf.find('div', class_="wiki_list_left")
    contents_list = contents.find_all('li')
    for each in contents_list:
        list_title = each.find('span', class_="list_title").get_text()

        sec_bady = each.find_all('a')
        sec_title = [i.string for i in sec_bady]
        sec_url = [i.get('href') for i in sec_bady]

        lenth = len(sec_title)

        result = [[list_title] * lenth, sec_title, sec_url]
        df = pd.DataFrame(result)
        result_df = df.T
        result_df.to_csv('jiaju_baike_contents.csv', mode='a', index=False, header=False)


def get_info_each_kind(url):
    bf = visit_web(url)

    page_list = bf.find('div', class_='page_lists')

    if page_list:
        pages = page_list.find_all('a')
        end_page = pages[-2].string
    else:
        end_page = 1

    result_url, result_title, result_time = [], [], []
    for i in range(int(end_page)):
        if i == 0:
            page_url = url
        else:
            page_url = url + "/p" + str(i)

        page_bf = visit_web(page_url)

        text_content = page_bf.find_all('div', class_="font_content")
        text_url = ['https://www.jiajuol.com' + i.find('a').get('href') for i in text_content]
        title = [i.find('a').string for i in text_content]

        pub_time = [i.find('i').get_text() for i in text_content]

        result_title.extend(title)
        result_url.extend(text_url)
        result_time.extend(pub_time)

        result = [result_title, result_url, result_time]
        print(url)
        print(result)
        return result


# get_big_kind_url('https://www.jiajuol.com/baike/cs15')

content_url = pd.read_csv('jiaju_baike_contents.csv', header=None)

for i in range(len(content_url)):
    url = 'https://www.jiajuol.com' + content_url.iloc[i, 2]
    result = get_info_each_kind(url)
    big_kind, small_kind = content_url.iloc[i, 0], content_url.iloc[i, 1]

    lenth = len(result[0])

    current_time = datetime.date.today()
    all_info = [[big_kind] * lenth, [small_kind] * lenth, [current_time] * lenth]
    all_info.extend(result)

    # print(all_info)
    df = pd.DataFrame(all_info)

    result_df = df.T

    result_df.to_csv('jiajubaike_detail.csv', mode='a', index=False, header=False)

    print(i)

print('end')


# get_info_each_kind('https://www.jiajuol.com/baike/cs4')