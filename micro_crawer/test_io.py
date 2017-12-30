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
content = ''
with open(file = sys.path[0] + '/data/target.html', mode='r', encoding='utf-8') as file :
    list = file.readlines()
    for line in list :
        content += line

print(content)

soup = BeautifulSoup(content, 'html.parser')
positon_model = {}
city = soup.find_all(name = 'em', attrs={'class' : 'vline'})[1].find_parent().contents[0].string
salary = soup.find(name = 'span', attrs={'class' : 'badge'}).contents[0]
position_name = soup.find(name = 'h1', attrs={'class' : 'name'}).contents[0].string
# query = query_params['query']

positon_model['city'] = city
positon_model['salary'] = salary
positon_model['position_name'] = position_name

print(positon_model)