# -*- coding: utf-8 -*-
"""
   File Name：     fenghuang_video
   Description :    https://zhuanlan.zhihu.com/p/104598442
   date：          2020/2/16
"""
import requests
from bs4 import BeautifulSoup
import json
import threading
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}


def get_href(url):
    response = requests.get(url, headers=headers)
    data = re.findall('"data":{"data":(.*?),"total"', response.text, re.S)[0]
    items = json.loads(data)
    for item in items:
        title = item['title']
        VedioHtmlUrl = 'http:' + item['url']
        Guid = item['guid']
        print(title, VedioHtmlUrl, Guid)
        download_vedio(title, VedioHtmlUrl, Guid)


# "data":{"data":[
def download_vedio(title, VedioHtmlUrl, Guid):
    url = 'https://shankapi.ifeng.com/feedflow/getVideoAuthUrl/{0}/getVideoAuthPath_1?callback=getVideoAuthPath_1'.format(
        Guid)
    response = requests.get(url, headers=headers)
    results = json.loads(response.text.replace('getVideoAuthPath_1(', '').replace(')', ''))
    results = results['data']

    vedio_oparams = results['authUrl']

    vedio_url = 'http://183.230.72.65/video19.ifeng.com/video09/2020/02/16/s31448188-102-9987642-203434/index.m3u8?' + vedio_oparams
    response = requests.get(vedio_url, headers=headers)
    IndexTs = response.text.split('\n')[5:][::2]

    if not os.path.exists('./fenghuang_vedio'):
        os.mkdir('./fenghuang_vedio')

    for index in IndexTs:
        if len(index) != 0:
            TsUrl = 'http://183.230.72.65/video19.ifeng.com/video09/2020/02/16/s31448188-102-9987642-203434/' + index
            res = requests.get(TsUrl, stream=True, headers=headers)
            with open('fenghuang_vedio/{0}.mp4'.format(title.replace('|', '').replace('?', '')), 'ab') as f:
                f.write(res.content)
                f.flush()


def main():
    pagenum = 3
    for i in range(1, pagenum):
        url = 'https://shankapi.ifeng.com/shanklist/getVideoStream/{}/24/27-95144-/1/getVideoStream?callback=getVideoStream'.format(
            i)
        get_href(url)
        # t = threading.Thread(target=get_href, args=(url,))
        # t.start()


if __name__ == '__main__':
    main()
