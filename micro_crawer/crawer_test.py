import urllib.request
import http.cookiejar

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
    'pn':'1',
    'kd':'机器学习'
}

params_data = urllib.parse.urlencode(params_data)

post_data = {
    'city':'杭州',
    'needAddtionalResult':'false',
    'isSchoolJob':'0'
}
post_data = urllib.parse.urlencode(post_data).encode('utf-8')

base_url = 'https://www.lagou.com/jobs/positionAjax.json?'
target_url = base_url + params_data

req = urllib.request.Request(url = target_url,data = post_data, method = 'POST', headers=headers_data)
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))