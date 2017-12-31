# -*- coding:utf-8 -*-
#coding=utf-8
import urllib.request
import http.cookiejar
import json,os,sys
import requests
from bs4 import BeautifulSoup

class LagouCrawer :
    def __init__(self) :
        print('爬虫已经启动...请稍等')
        self.headers = self.load_json_file(sys.path[0] + '/' + 'headers.json')
        self.encode_headers = urllib.parse.urlencode(self.headers)
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?'

    # def crawer_key_word(self, keyword) :
    def build_url(self, keyword, page_index) :
        self.params_data = {
            'first':'true',
            'kd':keyword,
            'pn' : str(page_index)
        }
        self.target_url = self.url + urllib.parse.urlencode(self.params_data)

    def crawer_search(self, keyword, city) :
        if keyword is None or city is None :
            return 'params error'
        self.post_data = {
            'city':city,
            'needAddtionalResult':'false',
            'isSchoolJob':'0'
        }
        self.encode_post_data = urllib.parse.urlencode(self.post_data).encode('utf-8')
        page_index = 1
        position_list = []
        while True :
            self.build_url(keyword, page_index)
            resp = self.request()
            try :
                result = json.loads(resp.read().decode('utf-8'))
                position_resp_list = result['content']['positionResult']['result']
                if len(position_resp_list) == 0 :
                    print("一共 :" + str(page_index - 1) + "页")
                    break
                print('爬取 --- > ' + str(page_index) + '页')
                for position in position_resp_list :
                    position_list.append(position)
            except Exception as e :
                print("请求错误")
            page_index += 1

        return position_list

    def request(self) :
        try :
            req = urllib.request.Request(url = self.target_url, headers = self.headers, data = self.encode_post_data, method = 'POST')
            return urllib.request.urlopen(req)
        except Exception as e:
            print(e)
            print("http error")

    def load_json_file(self, path) :
        try :
            file = open(file = path, mode = 'r', encoding = 'utf-8')
            return json.load(file)
        except IOError as err:
            print("open file error")
            print(err)

    def print_result(self, position_list) :
        print("职位数量为 : " + str(len(position_list)))
        for position in position_list :
            print("职位名称 :" + position['positionName'] + ",    公司名称 : " + position['companyFullName'] + ",   公司城市:" + position['city'] + '   薪资:' + position['salary'])
        
    def store_file(self, path, list) :
        try :
            file = open(path, mode='a')
            for p in list :
                try :
                    for k in p.keys() :
                        file.write(k + '=' + str(p[k]))
                    file.write('\n')
                except Exception as e :
                    print(e)
            file.close()
        except Exception as e :
            print(e)
            print("写入失败")


## 
# lagou_crawer = LagouCrawer()
# list = lagou_crawer.crawer_search('机器学习','成都')
# lagou_crawer.print_result(list)
# lagou_crawer.store_file(sys.path[0] + '/' + 'lagou.txt', list)


url = 'https://www.lagou.com/jobs/positionAjax.json'

def load_json_file(path) :
        try :
            file = open(file = path, mode = 'r', encoding = 'utf-8')
            return json.load(file)
        except IOError as err:
            print("open file error")
            print(err)

headers_file = load_json_file(sys.path[0] + '/headers.json')
list_headers = headers_file['position_list_headers']
detail_headers = headers_file['detail_page_headers']
params = {
    'city':'杭州',
    'needAddtionalResult':'false',
    'isSchoolJob':0
}

target_url = url + '?city=' + params['city'] +'&needAddtionalResult=' + params['needAddtionalResult'] + '&isSchoolJob=' + str(params['isSchoolJob'])

post_data = {
    'first':'true',
    'pn':1,
    'kd':'java'
}

# detail base
detail_base_url = 'https://www.lagou.com/jobs/'

result = requests.post(url = target_url, headers = list_headers, data = post_data)
if result.status_code == 200 :
    # print(result.text)
    position_list = json.loads(result.text)['content']['positionResult']['result']
    if position_list is not None and len(position_list) > 0 :
        for p in position_list :
            detail_id = p['positionId']
            detail_url = detail_base_url + str(detail_id) + '.html'
            detail_result = requests.get(url = detail_url, headers = detail_headers)
            if detail_result.status_code == 200 :
                # print html body
                print(detail_result.text)
                soup = BeautifulSoup(detail_result.text.encode(detail_result.encoding).decode('utf-8'), 'html.parser')
                position_name = soup.find(name = 'span', attrs={'class' : 'ceil-job'}).text
                salary = soup.find(name = 'span', attrs={'class' : 'ceil-salary'}).text
                detail_info = soup.find(name = 'h3', attrs={'class' : 'description'}).find_next_sibling().text

                postion = {
                    'position_name' : position_name,
                    'salary' : salary,
                    'detail_info' : detail_info,
                    'city' : params['city'],
                    'type' : post_data['kd']
                }

                print(postion)