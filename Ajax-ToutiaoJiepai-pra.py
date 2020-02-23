# -*- coding: utf-8 -*-
"""
   File Name：     Ajax-ToutiaoJiepai-pra
   Description :
   date：          2020/2/11
"""
import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import time


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    # print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_image(json):
    results = []
    title = ""
    image_list = []
    if json.get('data'):
        data = json.get('data')
        for item in data:
            urls = []
            if item.get('title'):
                title = item["title"]
            if item.get('title'):
                image_list = item["image_list"]
            for image in image_list:
                # print(title + ": " + image['url'])
                # print(image)
                urls.append(image['url'])

            result = {
                'title': title,
                'images': urls
            }
            results.append(result)
    return results


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        for image in item.get('images'):
            response = requests.get(image)
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Download', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    # img_list = json['data'][0]["image_list"]
    # for img in img_list:
    #     print(img['url'])
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    try:
        # for i in range(1, 11):
        #     main(i * 20)
        #     time.sleep(2)
        pool = Pool()
        groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
        pool.map(main, groups)
        pool.close()
        pool.join()

    except OSError:
        print('[Errno 22] 文件名、目录名或卷标语法不正确')
