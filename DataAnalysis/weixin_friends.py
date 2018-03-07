# -*- coding: utf-8 -*-
from wxpy import *
import codecs
import json


# Bot 的 chats(), friends()，groups(), mps() 方法, 可分别获取到当前机器人的 所有聊天对象、好友、群聊，以及公众号列表
# 初始化登陆 bot = Bot()


# wxpy.api.chats.chats.Chats对象是多个聊天对象的合集，可用于搜索或统计，
# 可以搜索和统计的信息包括sex(性别)、province(省份)、city(城市)和signature(个性签名)等。

# 通过friends()获取到所有好友信息，myfriends = bot.friends()


def log_in():
    bot = Bot()
    friends = bot.friends()
    return friends


def get_sex_distribution(friends):
    sex_dic = {'male': 0, 'famale': 0}
    for friend in friends:
        if friend.sex == 1:
            sex_dic['male'] += 1
        elif friend.sex == 2:
            sex_dic['famale'] += 1
    print(sex_dic)
    return sex_dic


def province_distribution(friends):
    provinces = []
    province_dict = {}
    for friend in friends:
        province_name = friend.province
        if province_name in provinces:
            province_dict[province_name] += 1
        else:
            provinces.append(province_name)
            province_dict[province_name] = 1
    print(province_dict)
    return province_dict


def get_signature(friends):
    f = open('./message/signature.txt', 'a', encoding='utf-8')      # encoding 注意编码格式
    for friend in friends:
        f.write(friend.signature + '\n')


if __name__ == '__main__':
    friends = log_in()
    sex_dic = get_sex_distribution(friends)
    f1 = open('./message/sex.txt', 'w', encoding='utf-8')
    f1.write(str(sex_dic))
    province_dic = province_distribution(friends)
    f2 = open('./message/province.txt', 'w', encoding='utf-8')
    f2.write(str(province_dic))
    get_signature(friends)
    print("end.....")













