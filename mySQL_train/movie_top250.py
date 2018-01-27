import requests
from bs4 import BeautifulSoup
import pymysql
import time

url1 = "https://movie.douban.com/top250?start=0&filter="
url2 = "https://movie.douban.com/top250?start=25&filter="

# 每页的request url
# for i in range(10):
#     page = i * 25
#     page_url = "https://movie.douban.com/top250?start=%d&filter=" % page
#     # print(page_url)


# 每页解析，获取信息（排名、片名、年份、国家、类型、标签、评分、评论人数、是否可播放）


def insert_into_mysql(movie_infor):
    """单条记录插入"""
    coon = pymysql.connect(host="localhost", user="root", password="root", database="test", port=3306, charset="utf8")

    sql_insert = "INSERT INTO movie " \
                 "(number, name, link_url, years, country, labels, player, score, comments_num, quote) " \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cur = coon.cursor()
    try:
        cur.execute(sql_insert, movie_infor)
        coon.commit()
    except Exception as e:
        print("排名为 " + str(movie_infor[0]) + "插入失败" + str(e))
    finally:
        cur.close()
        coon.close()


def get_each_movie_infor(each_movie):

    number = int(each_movie.find('em').string)

    # 片名--string
    name = each_movie.find('span', attrs={'class': 'title'}).string

    # 链接--string
    link_url = each_movie.a.attrs['href']

    info_list = each_movie.find('p').contents[2].string.strip().split('/')

    # 年份
    try:
        years = int(info_list[0].strip()[:4])
    except Exception as e_year:
        print(name + "查询出现错误,为： " + e_year)

    # 国家
    country = info_list[1]

    # 标签
    labels = info_list[2]

    # 有无播放源
    player = each_movie.find('span', attrs={'class': 'playable'})
    if player:
        player = "是"
    else:
        player = "否"

    score_info = each_movie.find('div', attrs={'class': 'star'})
    # 评分
    score = float(score_info.find('span', attrs={'class': 'rating_num'}).string)

    # 评论数
    comments_num = int(score_info.find_all('span')[-1].string[:-3])

    # 简介
    quote = each_movie.find('span', attrs={'class': 'inq'})
    if quote:
        quote = quote.string
    else:
        quote = None

    # 汇总
    movie_infor = (number, name, link_url, years, country, labels, player, score, comments_num, quote)
    # print(movie_infor)
    return movie_infor


def each_page_infor(page_url):
    response = requests.get(page_url)
    html_data = response.text.encode(response.encoding).decode('utf-8')
    bf = BeautifulSoup(html_data, 'html.parser')
    all_moive_items = bf.find_all('div', class_='item')
    for each_movie in all_moive_items:
        each_infor = get_each_movie_infor(each_movie)
        print(each_infor)
        # try:
        #     insert_into_mysql(each_infor)
        # except Exception:
        #     pass


def get_infor_from_web(url):
    for i in range(10):
        page = i * 25
        page_url = url % page
        try:
            each_page_infor(page_url)
            print("完成第" + str(i + 1) + "页")
        except Exception as e:
            print("第" + str(i + 1) + "页出错" + str(e))

        time.sleep(3)
    print('end')


# 网页模板
url = "https://movie.douban.com/top250?start=%d&filter="

if __name__ == '__main__':
    get_infor_from_web(url)
    print("完成")
