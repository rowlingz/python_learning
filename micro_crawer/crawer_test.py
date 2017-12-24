# -*- coding:utf-8 -*-
import urllib.request
import http.cookiejar
import json,os,sys

# ---- python 2 -----
# 获取cookie
# cookie = cookielib.MozillaCookieJar()
# ## 根据cookie获得handler
# urllib.HTTPCookieProcessor(cookie)
# # handler = urllib.HTTPCookieProcessor(cookie)
# # opener = urllib.build_opener(handler)
# ## 根据handler获取opener
# def getCookieUrl(target_url) :
#     # resp = urllib2.urlopen(target_url)
#     return opener.open(target_url).read()

# def ajaxUrl(position_url) :
#     return opener.open(position_url).read()

# getCookiesResp = getCookieUrl("https://www.lagou.com/jobs/positionAjax.json?first=true&pn=1&kd=机器学习")
# positionResp = ajaxUrl("https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false&isSchoolJob=0")
# print(positionResp)


# --- python 3 --
# 发送请求
# data = urllib.request.urlopen("http://www.baidu.com").read()
# ## 解码
# data = data.decode("UTF-8")
# ## 打印
# print(data)


# 爬baidu的tensorflow关键字返回
# key_map = {}
# key_map['wd'] = 'tensorflow'
# key_map_url = urllib.parse.urlencode(key_map)
# base_url = 'http://www.baidu.com/s?'
# url = base_url + key_map_url
# print('request url : ' + url)
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print('response : ' + data)


# lagou
def load_json_file(path) :
    try :
        file = open(file = path, mode = 'r', encoding = 'utf-8')
        return json.load(file)
    except IOError as err:
        print("open file error")
        print(err)

headers_data = load_json_file(sys.path[0] + '/' + 'headers.json')
encode_headers = urllib.parse.urlencode(headers_data)
url = 'https://www.lagou.com/jobs/positionAjax.json?first=true&pn=1&kd=机器学习'
params_data = {
    'first':'true',
    'kd':'算法'
}

post_data = {
    'city':'杭州',
    'needAddtionalResult':'false',
    'isSchoolJob':'0'
}
post_data = urllib.parse.urlencode(post_data).encode('utf-8')

base_url = 'https://www.lagou.com/jobs/positionAjax.json?'

page_index = 1
position_list = []
while True :
    ## 每一页去爬，空就break
    params_data['pn'] = str(page_index)
    encode_params_data = urllib.parse.urlencode(params_data)
    target_url = base_url + encode_params_data
    ## 获取职位列表
    req = urllib.request.Request(url = target_url,data = post_data, method = 'POST', headers=headers_data)
    resp = urllib.request.urlopen(req)
    # print(resp.read().decode('utf-8'))

    result = json.loads(resp.read().decode('utf-8'))
    position_resp_list = result['content']['positionResult']['result']
    if len(position_resp_list) == 0 :
        print('一共 : ' + str(page_index - 1) + "页")
        break
    for position in position_resp_list :
        position_list.append(position)
    page_index += 1

print("职位数量:" + str(len(position_list)))
for position in position_list :
    print("职位名称 :" + position['positionName'] + ", 公司名称 : " + position['companyFullName'] + ",公司城市:" + position['city'] + '薪资:' + position['salary'])

[{
    'positionName' : '',
    'city' : '',
    'description' : '',
    'company' : '',
    'salary' : ''
}]