import requests
from bs4 import BeautifulSoup
import pymysql

url1 = "https://movie.douban.com/top250?start=0&filter="
url2 = "https://movie.douban.com/top250?start=25&filter="

# 每页的request url
for i in range(10):
    page = i * 25
    page_url = "https://movie.douban.com/top250?start=%d&filter=" % page
    # print(page_url)


# 每页解析，获取信息（排名、片名、年份、国家、类型、标签、评分、评论人数、是否可播放）
response = requests.get(url1)
html_data = response.text.encode(response.encoding).decode('utf-8')
bf = BeautifulSoup(html_data, 'html.parser')
all_moive_items = bf.find_all('div', class_='item')

# i = 1
# for each_moive in all_moive_items:
#     print(i)


def insert_into_mysql(table, movie_infor):
    coon = pymysql.connect(host="localhost", user="root", password="root", database="test", port=3306, charset="utf8")

    sql_insert = "INSERT INTO %s VALUES %s"

    cur = coon.cursor()
    cur.execute(sql_insert, (table, movie_infor))
    cur.close()
    coon.commit()
    coon.close()


def get_each_movie_infor(each_movie):
    number = each_moive.find('em').string

    # 片名
    name = each_moive.find('span', attrs={'class': 'title'}).string

    # 链接
    link_url = each_moive.a.attrs['href']

    info_list = each_moive.find('p').contents[2].string.strip().split('/')

    # 年份
    years = int(info_list[0].strip())

    # 国家
    country = info_list[1]

    # 标签
    labels = info_list[2]

    # 有无播放源
    player = True
    if each_moive.find('playable') is None:
        player = False

    score_info = each_moive.find('div', attrs={'class': 'star'})
    # 评分
    score = float(score_info.find_all('span')[1].string)
    # 评论数
    comments_num = int(score_info.find_all('span')[-1].string[:-3])

    # 简介
    quote = each_moive.find('span', attrs={'class': 'inq'}).string

