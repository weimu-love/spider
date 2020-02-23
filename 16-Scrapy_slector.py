# -*- coding: utf-8 -*-
"""
   File Name：     16-Scrapy_slector
   Description :    https://cuiqingcai.com/8350.html
   date：          2020/2/14
"""
from scrapy import Selector

body = '<html><head><title>Hello World</title></head><body></body></html>'
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)

# 利用scrapy shell学习selector
# scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html
