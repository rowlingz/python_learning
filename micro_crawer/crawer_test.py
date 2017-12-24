# -*- coding:utf-8 -*-
import urllib.request
import http.cookiejar
import json

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
headers_data = {
            'Host': 'www.lagou.com',
            'Connection': 'keep-alive',
            'Content-Length': '55',
            'Origin': 'https://www.lagou.com',
            'X-Anit-Forge-Code': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application / json, text / javascript, * / *q = 0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer':'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cookie':'user_trace_token=20171013151921-d51c4d7f-afe6-11e7-920c-525400f775ce; LGUID=20171013151921-d51c5013-afe6-11e7-920c-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; JSESSIONID=ABAAABAAADEAAFID0A2F9D4C53C2572C1BD02B23793DCBC; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513157294; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514042023; _ga=GA1.2.846894165.1513157294; _gid=GA1.2.120579721.1514041858; LGSID=20171223231053-77ef3561-e7f3-11e7-9e2e-5254005c3644; LGRID=20171223232433-60b446e3-e7f5-11e7-9e2e-5254005c3644; SEARCH_ID=4e84a847c1cb4755b09c7daed9a82295'
}
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

# "createTime":"2017-12-22 10:31:14",
#                     "companyId":51649,
#                     "positionId":3587720,
#                     "positionName":"机器学习工程师",
#                     "education":"硕士",
#                     "city":"杭州",
#                     "financeStage":"B轮",
#                     "companyShortName":"掌众金服",
#                     "companyLogo":"i/image/M00/0D/9E/CgpEMljl4JCAB4NsAAAT2z7aW8s078.jpg",
#                     "salary":"22k-44k",
#                     "industryField":"移动互联网,金融",
#                     "district":"西湖区",
#                     "positionAdvantage":"福利待遇好,双休,工作环境佳",
#                     "companySize":"500-2000人",
#                     "companyLabelList":[
#                         "技能培训",
#                         "节日礼物",
#                         "绩效奖金",
#                         "年度旅游"
#                     ],
#                     "publisherId":1859504,
#                     "score":0,
#                     "jobNature":"全职",
#                     "workYear":"3-5年",
#                     "approve":1,
#                     "positionLables":[
#                         "风控",
#                         "大数据",
#                         "深度学习"
#                     ],
#                     "industryLables":[

#                     ],
#                     "businessZones":null,
#                     "formatCreateTime":"2天前发布",
#                     "imState":"today",
#                     "lastLogin":1514001372000,
#                     "explain":null,
#                     "plus":null,
#                     "pcShow":0,
#                     "appShow":0,
#                     "deliver":0,
#                     "gradeDescription":null,
#                     "promotionScoreExplain":null,
#                     "firstType":"金融类",
#                     "secondType":"风控",
#                     "isSchoolJob":0,
#                     "subwayline":null,
#                     "stationname":null,
#                     "linestaion":null,
#                     "latitude":"30.281044",
#                     "longitude":"120.069178",
#                     "companyFullName":"北京掌众科技有限公司",
#                     "adWord":0

[{
    'positionName' : '',
    'city' : '',
    'description' : '',
    'company' : '',
    'salary' : ''
}]