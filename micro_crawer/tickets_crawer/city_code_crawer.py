#-*- coding:utf-8 -*-
import requests
import sys
import os
import json
resp = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9044')
resp_js = resp.text.encode(resp.encoding).decode('utf-8')
list = resp_js.split('@')

_city_code_dic = {}
for city_info in list[1:] :
    city_info_list = city_info.split('|')
    _city_code_dic[city_info_list[1]] = city_info_list[2]


print(_city_code_dic)
file = open(file = '/Users/mapeichuan/Github/python_learning/micro_crawer/data/12306_city_code.txt', mode='w', encoding = 'utf-8')
for k in _city_code_dic :
    line = k + '=' + _city_code_dic.get(k)
    file.writelines(line + '\n')
    
# with open( "/Users/mapeichuan/Github/python_learning/micro_crawer/data/12306_city_code.json", mode='w') as file :
#     file.write(json.dumps(_city_code_dic,encoding = "utf-8"))
    # json.dump(_city_code_dic, file, ensure_ascii = False)
## 输入城市
input = '杭州'
code = _city_code_dic.get(input)
print(code)


# 以字典形式存/取文件
resp = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?'
                    'station_version=1.9044')
resp_str = resp.text        # str格式
total_info = resp_str.split('@')
# print(total_info)

city_code_dic = {}
for city_info in total_info[1:]:
    city_info_lis = city_info.split("|")
    city_code_dic[city_info_lis[1]] = city_info_lis[2]

# 以字典形式存储在json文件中
file_name = "_city_code.json"
with open(file_name, 'w', encoding='utf-8') as f_obj:
    f_obj.write(json.dumps(city_code_dic, ensure_ascii=False))


def get_code_to_city(city):
    with open(file_name, encoding='utf-8') as f_city_code:
        code_city = json.load(f_city_code)

    # 该城市全部站名
    for name in code_city.keys():
        if city in name:
            print(name + "--->" + code_city[name])

    return code_city[city]


city_name = input("请输入出发城市： ")
print(city_name + "对应code: " + get_code_to_city(city_name))
