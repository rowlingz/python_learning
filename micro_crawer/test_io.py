import sys
# file = open(file = sys.path[0] + '/data/boss.txt', mode='w')
# for i in range(0, 11) :
#     file.write(str(i))
# file.close()
# with open(file = sys.path[0] + '/data/boss.txt', mode='w') as file :
#     file.write('kkkkk\n')
#     file.write('aaa')

# with open(file = sys.path[0] + '/data/boss.txt', mode='r', encoding='utf-8') as file :
#     list = file.readlines()
#     for p in list :
#         print(p)


## 标签解析
from bs4 import BeautifulSoup
import json
import requests
content = ''
with open(file = sys.path[0] + '/headers.json', mode='r', encoding='utf-8') as file :
    list = file.readlines()
    for line in list :
        content += line

print(content)

# 测试解析boss 页面

# soup = BeautifulSoup(content, 'html.parser')
# positon_model = {}
# city = soup.find_all(name = 'em', attrs={'class' : 'vline'})[1].find_parent().contents[0].string
# salary = soup.find(name = 'span', attrs={'class' : 'badge'}).contents[0]
# position_name = soup.find(name = 'h1', attrs={'class' : 'name'}).contents[0].string
# # query = query_params['query']

# positon_model['city'] = city
# positon_model['salary'] = salary
# positon_model['position_name'] = position_name

# print(positon_model)

## 测试解析拉勾

# position_list = content['content']['positionResult']['result']

# detail_base_url = 'https://www.lagou.com/jobs/3900913.html'
# headers = json.loads(content)
# result = requests.get(url = detail_base_url, headers = headers)
# print(result.text)

## 开始解析lagou_detail
content = ''
with open(sys.path[0] + '/data/lagou_detail.html', mode='r', encoding = 'utf-8') as file :
    list = file.readlines()
    for c in list :
        content += c

print(content)

soup = BeautifulSoup(content, 'html.parser')
position_name = soup.find(name = 'span', attrs={'class' : 'ceil-job'}).text
salary = soup.find(name = 'span', attrs={'class' : 'ceil-salary'})
detail_info = soup.find(name = 'h3', attrs={'class' : 'description'}).find_next_sibling().text

print('end')
