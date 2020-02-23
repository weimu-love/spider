# -*- coding: utf-8 -*-
from urllib.parse import quote
from scrapy import Request, Spider
from scrapyseleniumtest.items import ProductItem
import re


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                print(url)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        # print(type(response.body))

        res = str(response.body, encoding='utf-8')
        result = re.findall('"itemlist":(.*?);\n\s+g_srp_loadCss', res, re.S)[0]
        data = re.findall('"auctions":\[(.*?)\],"recommendAuctions"', result, re.S)[0]

        titles = re.findall('"pid":"","title":"(.*?)","raw_title"', data, re.S)
        pic_urls = re.findall('"pic_url":"(.*?)","detail_url"', data, re.S)
        prices = re.findall('"view_price":"(.*?)","view_fee"', data, re.S)
        locations = re.findall('"item_loc":"(.*?)","', data, re.S)
        shops = re.findall('"nick":"(.*?)","', data, re.S)

        for title, pic_url, price, location, shop in zip(titles, pic_urls, prices, locations, shops):
            item = ProductItem()
            item['image'] = 'https:' + pic_url.strip()
            item['price'] = price.strip()
            item['title'] = re.sub('<span.*>|</span>', '', title).strip()
            item['shop'] = shop.strip()
            item['location'] = location.strip()
            yield item


