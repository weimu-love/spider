# -*- coding: utf-8 -*-
"""
   File Name：     xiaohua-pra
   Description :
   date：          2020/2/17
"""
import requests
from lxml import etree
import os
import time
import threading

BASE_URL = 'http://www.521609.com/daxuemeinv/list8'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
PAGE = 23


def get_img_urls(url):
    res = requests.get(url, headers=HEADERS)
    # print(res.text)

    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    img_urls = html.xpath('//div[@id="content"]//div[contains(@class,"index_img")]//img/@src')
    titles = html.xpath('//div[@id="content"]//div[contains(@class,"index_img")]//a[@class="title"]//text()')
    # print(len(img_urls), len(titles))

    for img_url, title in zip(img_urls, titles):
        yield {
            'img_url': 'http://www.521609.com' + img_url.replace('-lp', ''),
            'title': title.replace(' ', '')
        }


def download_img(img_url, title):
    if not os.path.exists('./xiaohua'):
        os.mkdir('./xiaohua')

    file_path = './xiaohua/' + title + '.jpg'
    res = requests.get(img_url, headers=HEADERS)
    with open(file_path, 'wb') as f:
        f.write(res.content)


def main():
    for page in range(PAGE):
        url = BASE_URL + str(page + 1) + '.html'
        print('列表页： ' + url)

        threads = []
        imgs = get_img_urls(url)
        for img in imgs:
            print('下载中： ' + img['img_url'])
            t = threading.Thread(target=download_img, args=(img['img_url'], img['title']))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        time.sleep(2)


if __name__ == '__main__':
    main()
