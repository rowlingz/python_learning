# -*- coding:utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import json
import time,random
import crawer_dao

# print(sys.modules.keys())
# for k in sys.modules.keys() :
#     if k == 'requests' :
#         print('存在requests模块')
#         exit(0)
# print('不存在')

# result = requests.get('http://www.yinyuetai.com/')
# # test requests lib
# if (result.status_code == 200) :
#     print(result.text.encode(result.encoding).decode('utf-8'))
url = 'http://www.zhipin.com'
base_url = url + '/job_detail/?'
query_params = {
    'query':'Java',
    'scity':'101210100',
    'source':'1'
}
dao = crawer_dao.position_dao()
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'__jsluid=305fc5ddb82198863097faff98191fd5; __c=1514292510; sid=sem_pz_bdpc_index; __g=sem_pz_bdpc_index; lastCity=101210100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1514292691,1514297188,1514526794; __l=r=http%3A%2F%2Fwww.zhipin.com%2F&l=%2Fjob_detail%2F%3Fquery%3D%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%26scity%3D101210100%26source%3D2&g=%2F%3Fsid%3Dsem_pz_bdpc_index; JSESSIONID=""; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F1416517406.html%3Fka%3Dsearch_list_1; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1514649888; __a=67060313.1514292510..1514292510.24.1.24.22',
    'Host':'www.zhipin.com',
    'Referer':'http://www.zhipin.com/job_detail/?query=%E7%AE%97%E6%B3%95&scity=101210100&source=2',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
proxies = {'HTTP', 'http://118.193.107.36:80'}
page_index = 7
# with open(file = sys.path[0] + '/data/boss.txt', mode='w') as file :
while True :
    query_params['page'] = page_index
    print('开始爬取 ---- > ' + str(page_index) + '页')
    try :
        result = requests.get(url = 'http://www.zhipin.com/job_detail/?query=%E7%AE%97%E6%B3%95&scity=101210100&source=2' , params = query_params, headers = headers, proxies = None)
    except Exception as err:
        print(' request error ')
        exit(0)
    if result.status_code == 200 :
        # print(result.text.encode(result.encoding).decode('utf-8'))
        html_body = result.text.encode(result.encoding).decode('utf-8')
        ## 打印整个文本
        # print(html_body)
        soup = BeautifulSoup(html_body,'html.parser')
        ## 打印指定标签
        # print(soup.li)
        ## prettify打印html文件内容
        # print(soup.prettify())
        position_list = soup.find_all(name = 'a')
        ## 跳转链接
        content_url_list = []
        for position in position_list :
            if len(position.get('href')) >= 12 and '/job_detail/' == position.get('href')[0:12] :
                content_url_list.append(position.get('href'))
        if len(content_url_list) == 0 :
            break
        ## 爬取每个页面的描述k -> 链接, v -> 描述
        desp_map = {}
        for content_url in content_url_list :
            next_url = url + content_url
            print('request position detail , url ' + next_url + ', random sleep ')
            time.sleep(random.randint(3,5))
            print('restart crawer...')
            result = requests.get(url = next_url, params=None, headers = headers)
            if result.status_code == 200 :
                try :
                    html_body = result.text.encode(result.encoding).decode('utf-8')
                    soup = BeautifulSoup(html_body, 'html.parser')
                    ## 每个具体页面
                    positon_model = {}
                    ## 解析html
                    city = soup.find_all(name = 'em', attrs={'class' : 'vline'})[1].find_parent().contents[0].string
                    salary = soup.find(name = 'span', attrs={'class' : 'badge'}).contents[0]
                    position_name = soup.find(name = 'h1', attrs={'class' : 'name'}).contents[0].string
                    query = query_params['query']

                    positon_model['city'] = city
                    positon_model['salary'] = salary
                    positon_model['position_name'] = position_name
                    positon_model['type'] = query
                    desc_list = soup.find_all(name = 'div', attrs={'class' : 'text'})
                    desp = None
                    if desc_list is not None and len(desc_list) > 0 :
                        for desc in desc_list :
                            print(desc.text)
                            print('--------- 分割线 --------')
                            desp_map[url] = desc.text
                            desp = desc.text
                    if desp is not None :
                        positon_model['detail_info'] = desp
                    result = dao.insert_position(positon_model)
                    if result :
                        print('insert ok ')
                    else :
                        print('dao error')
                except Exception as err :
                    print(err)
                    continue
            else :
                print('http status -> ' + str(result.status_code) + ', reason -> ' + result.reason)
                break
        page_index += 1
    elif result.status_code == 403 :
        print('服务被拒绝了')
        break
    else :
        print('http status = ' + str(result.status_code) + ", reason = " + result.reason)
        break

## IP被限制，考虑代理

position = {
    'city' : '成都',
    'position_name' : '测试职位',
    'detail_info' : '测试详细信息',
    'salary' : 10,
    'type' : '机器学习'
}

# dao = crawer_dao.position_dao()
# for i in range(10) : 
#     insert_result = dao.insert_position(position)
#     if insert_result :
#         print('插入成功')
#     else :
#         print('插入失败!!')