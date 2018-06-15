# -*- coding:utf-8 -*-
from urllib.parse import urlencode
import requests
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery'
    }

    url = "https://www.toutiao.com/search_content/?" + urlencode(params)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }


def save_images(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))

    try:
        response = requests.get('https:' + item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_images(item)


if __name__ == "__main__":
    pool = Pool()
    groups = ([i * 20 for i in range(0, 3)])
    pool.map(main, groups)
    pool.close()
    pool.join()
