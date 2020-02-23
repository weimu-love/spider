# -*- coding: utf-8 -*-
"""
   File Name：     xun-proxy
   Description :    http://www.xdaili.cn/buyproxy
   date：          2020/2/13
"""
import requests
import json


def crawl_xdaili(self):
    """
    获取讯代理
    :return: 代理
    """
    url = 'http://www.xdaili.cn/ipagent/greatRecharge/getGreatIp?spiderId=da289b78fec24f19b392e04106253f2a&orderno=YZ20177140586mTTnd7&returnType=2&count=20'
    html = requests.get(url).text
    if html:
        result = json.loads(html)
        proxies = result.get('RESULT')
        for proxy in proxies:
            yield proxy.get('ip') + ':' + proxy.get('port')
