# -*- coding:utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import json
import time,random
# print(sys.modules.keys())
# for k in sys.modules.keys() :
#     if k == 'requests' :
#         print('存在requests模块')
#         exit(0)
# print('不存在')


result = requests.get('http://www.yinyuetai.com/')
## test requests lib
# if (result.status_code == 200) :
#     print(result.text.encode(result.encoding).decode('utf-8'))
url = 'http://www.zhipin.com'
base_url = url + '/job_detail/?'
query_params = {
    'query':'算法',
    'scity':'101210100',
    'source':'1'
}
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'__c=1513169552; sid=sem_pz_bdpc_index; __jsluid=305fc5ddb82198863097faff98191fd5; __g=sem_pz_bdpc_index; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F1415739147.html%3Fka%3Dsearch_list_28; lastCity=101210100; __l=r=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fDNJKT0tHdU0KZEgsArcW7p00000cuj6-b000002M924Z.THdBULP1doZA80K85yF9pywdpAqVuNqsusK15ymYPA7-rHfLnj0snAnvrjm0IHdDrRD1nWIjwHIArHn1nbfzwRDYPDNDfHFaf1mdPHmsrfK95gTqFhdWpyfqn10vrjcknWb1nzusThqbpyfqnHm0uHdCIZwsrBtEILILQMGCpgKGUB4WUvYE5LPGujd1uydxTZGxmhwsmdqGUhw-X0KWThnqPWnYnWc%26tpl%3Dtpl_10085_15730_11224%26l%3D1501709190%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25259A%2525E6%25258D%2525A2%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525E5%2525B0%2525B1%2525E6%252598%2525AF%2525E6%25258D%2525A2Boss%2526xp%253Did(%252522m57155b2c%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D135%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1916%26prefixsug%3Dboss%26rsp%3D2&l=%2F%3Fsid%3Dsem_pz_bdpc_index%22&g=%2F%3Fsid%3Dsem_pz_bdpc_in; __a=41477629.1513169552..1513169552.16.1.16.16; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1513169553,1514210165; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1514210182',
    'Host':'www.zhipin.com',
    'Referer':'http://www.zhipin.com/job_detail/?query=%E7%AE%97%E6%B3%95&scity=101210100&source=2',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
page_index = 4
while True :
    query_params['page'] = page_index
    print('开始爬取 ---- > ' + str(page_index) + '页')
    result = requests.get(url = 'http://www.zhipin.com/job_detail/?query=%E7%AE%97%E6%B3%95&scity=101210100&source=2' , params = query_params, headers = headers)
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
                print('获取的url : ' + position.get('href'))
                content_url_list.append(position.get('href'))
        if len(content_url_list) == 0 :
            break
        ## 爬取每个页面的描述k -> 链接, v -> 描述
        desp_map = {}
        for content_url in content_url_list :
            next_url = url + content_url
            print('每个具体职位请求休眠一下')
            time.sleep(random.randint(3,5))
            print('启动...')
            result = requests.get(url = next_url, params=None, headers = headers)
            if result.status_code == 200 :
                html_body = result.text.encode(result.encoding).decode('utf-8')
                soup = BeautifulSoup(html_body, 'html.parser')
                desc_list = soup.find_all(name = 'div', attrs={'class' : 'text'})
                if desc_list is not None and len(desc_list) > 0 :
                    for desc in desc_list :
                        print(desc.text)
                        print('--------- 分割线 --------')
                        desp_map[url] = desc.text
            else :
                print('http status -> ' + str(result.status_code) + ', reason -> ' + result.reason)
                break
        page_index += 1
    elif result.status_code == 403 :
        print('服务被拒绝了')
    else :
        print('http status = ' + str(result.status_code) + ", reason = " + result.reason)
        break

## IP被限制，考虑代理