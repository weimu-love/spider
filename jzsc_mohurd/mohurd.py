# -*- coding: utf-8 -*-
"""
   File Name：     mohurd
   Description :
   date：          2020/2/22
"""
import requests
import execjs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Referer': 'http://jzsc.mohurd.gov.cn/data/company'
}
resp = requests.get('http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15&total=0')
t = resp.text

ctx = None
if ctx is None:
    with open('mohurd.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())

data = ctx.call('getData', t)
print(data)
