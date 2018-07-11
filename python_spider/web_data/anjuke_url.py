# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 区域-版块--价格-户型
# 爬取特定条件的url列表，并将其存入指定文件

def visit_web(url):
    """获取网页"""
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.139 Safari/537.36',
               }
    bf = None
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            html = response.text
            bf = BeautifulSoup(html, "html.parser")
    except requests.ConnectionError as e:
        error_message = pd.DataFrame({'url': url, 'error': e})
        error_message.to_csv('fail_url.csv', index=False, mode='a', encoding='utf_8_sig')
        # print(e)
    return bf


def get_items_list(url):
    """主区域"""
    bf = visit_web(url)
    if bf is None:
        return
    items_a = {}
    try:
        all_item = bf.find('div', class_='items')
        items_url = all_item.find_all('a')
        for item in items_url:
            items_a[item.string] = item.get('href')
        # print(items)
        # return items_a
    except AttributeError:
        print('error')
    return items_a


def get_sub_items(item_url):
    """二级区域"""
    bf = visit_web(item_url)
    sub_items = {}
    try:
        all_sub = bf.find('div', class_='sub-items')
        sub_list = all_sub.find_all('a')
        for sub in sub_list:
            sub_items[sub.string] = sub.get('href')
        # print(sub_items)
    except AttributeError:
        print('error')
    return sub_items


def get_price_items(url):
    bf = visit_web(url)
    price_items = {}
    try:
        all_price = bf.find_all('div', class_='items')[1]
        price_list = all_price.find_all('a')
        for price in price_list:
            price_items[price.string] = price.get('href')
        # print(price_items)
    except AttributeError:
        print('error')
    return price_items


def get_house_type(url):
    bf = visit_web(url)
    type_items = {}
    try:
        all_type = bf.find_all('div', class_='items')[3]
        type_list = all_type.find_all('a')
        for house_type in type_list:
            type_items[house_type.string] = house_type.get('href')
        # print(type_items)
    except AttributeError:
        print('error')
    return type_items


def get_all_condition_url(url, url_file):
    start_time = time.time()
    regions = get_items_list(url)
    url_list = []
    for region_name, region_url in regions.items():
        sub_regions = get_sub_items(region_url)
        for sub_name, sub_url in sub_regions.items():
            time.sleep(0.05)
            price_items = get_price_items(sub_url)
            for price_name, price_url in price_items.items():
                type_items = get_house_type(price_url)
                for type_name, type_url in type_items.items():
                    url_name = '-'.join([region_name, sub_name, price_name, type_name])
                    url_list.append([url_name, type_url])

        print('-'.join([region_name, sub_name]))
    url_df = pd.DataFrame(url_list, columns=['url_name', 'url'])
    url_df.to_csv(url_file, index=False, encoding='utf_8_sig')
    end_time = time.time()
    print(end_time - start_time)
    print('end')


if __name__ == '__main__':
    get_all_condition_url('https://hangzhou.anjuke.com/sale/', url_file='factor_url_hangzhou.csv')








