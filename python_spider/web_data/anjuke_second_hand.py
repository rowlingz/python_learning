# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time


# 获取指定网页下的房源信息

def visit_web(url):
    """获取网页"""
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.139 Safari/537.36'}
    bf = None
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            html = response.text
            bf = BeautifulSoup(html, "html.parser")
    except requests.ConnectionError as e:
        error_message = pd.DataFrame({'url': [url], 'error': [e]})
        error_message.to_csv('fail_url.csv', index=False, header=False, mode='a', encoding='utf_8_sig')
        # print(e)
    return bf


def get_info_each_page(bf, filename):
    """
    解析每一个有效网页的 内容
    :param bf: html;  html字符串
    :return: list; 某一页的信息列表[]
    将每页得信息存入 csv文件
    """
    try:
        house_mod = bf.find('ul', id='houselist-mod-new')
        house_list = house_mod.find_all('li', class_="list-item")

        results = []
        for house in house_list:
            title = house.find('a').get('title')
            title_url = house.find('a').get('href')

            icon_tag = house.find('em', class_='guarantee_icon1')
            icon_zt = house.find('i', class_='icon-tag icon-zt')
            if icon_tag:
                icon_tag = icon_tag.string
            if icon_zt:
                icon_zt = icon_zt.string

            house_detail = house.find_all('div', class_='details-item')
            message = house_detail[0].find_all('span')
            message_list = [i.get_text() for i in message]

            if len(house_detail) == 2:
                address = house_detail[1].find('span', class_='comm-address').get('title').split()
            else:
                address = [np.nan, np.nan]
            community_name = address[0]
            community_address = address[1]

            tags = house.find('div', class_='tags-bottom')
            if tags:
                tags = [i.string for i in tags.find_all('span')]

            price_det = house.find('span', class_='price-det').get_text()
            price_unit = house.find('span', class_='unit-price').string

            result = [title, title_url, icon_tag, icon_zt, message_list, community_name,
                      community_address, tags, price_det, price_unit]

            results.append(result)

        df = pd.DataFrame(results, columns=['title', 'title_url', 'icon_tag', 'icon_zt', 'message_list',
                                            'community_name', 'community_address', 'tags', 'price_det', 'price_unit'])
        # return df
        df.to_csv(filename, index=False, header=False, mode='a', encoding='utf_8_sig')
    except AttributeError:

        return


def all_info(url, filename):
    """
    访问某个条件下的 所有信息
    :param url: str, 某条件下的url
    :return:
    """
    bf = visit_web(url)
    if bf is None:
        return
    get_info_each_page(bf, filename)

    next_page = True
    while next_page:
        try:
            pages = bf.find('div', class_='multi-page')
            next_url = pages.find('a', class_='aNxt').get('href')
            # time.sleep(0.1)
            bf = visit_web(next_url)
            if bf:
                get_info_each_page(bf, filename)
            else:
                next_page = False
        except AttributeError:
            next_page = False


def run(url_file, info_file):
    star_time = time.time()
    df = pd.read_csv(url_file)
    nrows = len(df)
    for i in range(7723, nrows):
        url = df.loc[i, 'url']
        all_info(url, info_file)
        # if i % 10 == 0:
        #     time.sleep(0.1)
        print(i)
    end_time = time.time()
    print(end_time - star_time)
    print('end')


if __name__ == '__main__':
    run('factor_url_hangzhou.csv', 'hangzhou_info_2.csv')




