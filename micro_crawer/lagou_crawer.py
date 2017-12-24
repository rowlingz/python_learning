# -*- coding:utf-8 -*-
#coding=utf-8
import urllib.request
import http.cookiejar
import json,os,sys

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
            # file = open(path, mode='a')
            # for p in list :
            #     try :
            #         for k in p.keys() :
            #             file.write(k + '=' + str(p[k]))
            #         file.write('\n')
            #     except Exception as e :
            #         print(e)
            # file.close()
        except Exception as e :
            print(e)
            print("写入失败")


## 
lagou_crawer = LagouCrawer()
list = lagou_crawer.crawer_search('机器学习','成都')
lagou_crawer.print_result(list)
lagou_crawer.store_file(sys.path[0] + '/' + 'lagou.txt', list)

