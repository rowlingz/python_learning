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