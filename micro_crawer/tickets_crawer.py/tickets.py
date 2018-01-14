import requests

# re = requests.get('https://www.baidu.com')
# print(re)

base_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
params = {
    'leftTicketDTO.train_date':'2018-01-15',
    'leftTicketDTO.from_station':'HZH',
    'leftTicketDTO.to_station':'SHH',
    'purpose_codes':'ADULT'
}
resp = requests.get(url = base_url, params = params, headers = {
    'Host': 'kyfw.12306.cn',
    'Connection': 'keep-alive',
    "Cache-Control": "no-cache",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    'If-Modified-Since': '0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=C536FA468BF80E207CB65AE07D14632F; tk=5oYQPKz0KgI2LMV35JlULDy8Y6zNjz_Srq1XZw1pp2p0; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=267387402.24610.0000; RAIL_EXPIRATION=1516210200843; RAIL_DEVICEID=FRp5YDkkifyA7SIZY65m6uSOtT_qQCg79YLvzC8iCoouUqBnOgy7hCxBpvwuC7l5IY-mwSBOZUkCPdJHjiKyE8SWGKvtFBFJc9IVG76BefHq5-34grWgT-xEoDsqok9v09bUN5_KLRZe2VTwbSag-iGHXr4uDFdU; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toDate=2018-01-14; _jc_save_wfdc_flag=dc; BIGipServerpool_passport=401408522.50215.0000; current_captcha_type=Z; _jc_save_fromDate=2018-01-15; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_showIns=true'
})
if resp.status_code != 200 :
    print('error' + str(resp.reason))
    exit(0)

list = resp.json()['data']['result']
print('车次数目 -> ' + str(len(list)))

class Train_info :
    def __init__(self, name, is_enough) :
        self.name = name
        self.is_enough = is_enough

train_list = []

index = 0
for data in list :
    ## 处理每一趟列车信息
    if index > 5 :
        break
    content_list = data.split('|')
    print('车次 -> ' + content_list[3])
    # print('一等座 ' + )
    print('软卧 -> ' + content_list[23])
    print('硬卧 -> ' + content_list[26])
    print('硬座 -> ' + content_list[28])
    print('无座 -> ' + content_list[29])
    print('-----分割线----')
    index +=  1