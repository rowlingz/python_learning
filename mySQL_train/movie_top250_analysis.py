# coding = utf-8

import pymysql
import pandas as pd
import matplotlib.pyplot as plt


def get_data_from_mysql(table):
    """从mySQL中获取数据"""
    coon = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="test",
        port=3306,
        charset="utf8")
    sql_select = "SELECT * FROM " + table
    data = pd.read_sql(sql_select, coon,)
    data.columns = ['id', 'number', 'name', 'link_url', 'years',
                    'country', 'labels', 'player', 'score', 'comments_num', 'quote']
    print(data.describe())
    return data


def count_single(data):
    """属性值单一的进行计数"""
    value = []
    value_count = {}
    for sample in data:
        if sample not in value:
            value.append(sample)
            value_count[sample] = 1
        else:
            value_count[sample] += 1
    return value, value_count


def get_distribution(value, value_count, attributes):
    """属性分布图的绘制"""
    x = range(len(value))
    y = [i for i in value_count.values()]
    plt.bar(x, y, width=0.5)
    plt.xticks(x, value, size='small', rotation=90)
    plt.rcParams['font.sans-serif'] = ['FangSong']      # 设定默认字体
    plt.xlabel(attributes)
    plt.ylabel(attributes + 'counts')
    plt.title(attributes + "分布图")
    for a, b in zip(x, y):
        plt.text(a, b+0.1, '%d' % b, ha='center', va='bottom', fontsize=8)
    plt.savefig("image/ %s 分布图.png" % attributes)
    plt.show()


def years_analysis(data):
    years, years_count = count_single(data['years'])
    print(years_count)
    get_distribution(years, years_count, 'years')


def is_player_analysis(data):
    player, player_count = count_single(data['player'])
    print(player_count)
    get_distribution(player, player_count, 'player')


def country_analysis(data):
    countries = []
    countries_count = {}
    for i in data['country']:
        country = i.strip().split(' ')[0]
        if country not in countries:
            countries.append(country)
            countries_count[country] = 1
        else:
            countries_count[country] += 1

    get_distribution(countries, countries_count, 'country')
    # print(countries)
    print(countries_count)


def labels_analysis(data):
    style = []
    style_count = {}
    for labels in data['labels']:
        for label in labels.strip().split(' '):
            if label not in style:
                style.append(label)
                style_count[label] = 1
            else:
                style_count[label] += 1
    get_distribution(style, style_count, 'labels')
    print(style_count)


if __name__ == '__main__':
    data = get_data_from_mysql('movie')
    country_analysis(data)
    labels_analysis(data)
    years_analysis(data)
    is_player_analysis(data)


