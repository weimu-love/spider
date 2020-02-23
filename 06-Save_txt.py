# -*- coding: utf-8 -*-
"""
   File Name：     06-Save_txt
   Description :
   date：          2020/2/11
"""
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
# print(doc)
items = doc('.ExploreHomePage-collectionCard').items()
for item in items:
    # print(item)
    title = item.find('.ExploreCollectionCard-title').text()
    creator = item.find('.ExploreCollectionCard-creatorName').text()
    question = item.find('.ExploreCollectionCard-contentTitle').text()
    answer = item.find('.ExploreCollectionCard-contentExcerpt').text()
    with open('zhihu.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join([title, creator, question, answer]))
        f.write('\n' + '=' * 50 + '\n')
