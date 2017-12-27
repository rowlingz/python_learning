from bs4 import BeautifulSoup
import requests

result = requests.get('http://www.v2ex.com')

fangtang_url = 'https://sc.ftqq.com/SCU8990T23db6df13ddac6da6ec700e611b8821559391fe2cf0a8.send'

if result.status_code == 200 :
    soup = BeautifulSoup(result.text.encode(result.encoding).decode('utf-8'), 'html.parser')
    list = soup.find_all(name = 'span', attrs={'class' : 'item_title'})
    title = ''
    if len(list) > 0 :
        for item in list :
            title = title + item.a.text + '\n'
    result = requests.post(url = fangtang_url, data = {
        'text' : '标题',
        'desp' : title
    })
    if result.status_code != 200 :
        print('weChat error , ' + result.reason)
    print(title)
else :
    print('error , http code : ' + result.status_code)