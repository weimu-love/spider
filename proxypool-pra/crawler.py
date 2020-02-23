# -*- coding: utf-8 -*-
"""
   File Name：     Crawler
   Description :
   date：          2020/2/12
"""
import json
from utils import get_page
from bs4 import BeautifulSoup
import time


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    # def crawl_proxy360(self):
    #     """
    #     获取Proxy360
    #     :return: 代理
    #     """
    #     start_url = 'http://www.proxy360.cn/Region/China'
    #     print('Crawling', start_url)
    #     html = get_page(start_url)
    #     if html:
    #         doc = pq(html)
    #         lines = doc('div[name="list_proxy_ip"]').items()
    #         for line in lines:
    #             ip = line.find('.tbBottomLine:nth-child(1)').text()
    #             port = line.find('.tbBottomLine:nth-child(2)').text()
    #             yield ':'.join([ip, port])

    def crawl_xicidaili(self, page_count=4):
        start_url = 'https://www.xicidaili.com/nn/{}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        print(urls)

        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = BeautifulSoup(html, 'lxml')
                ip_list = doc.select('#ip_list tr')
                # print(type(ip_list))
                for i in range(1, len(ip_list)):
                    ip = ip_list[i]
                    tds = ip.find_all('td')
                    ip = str(tds[1].string).strip()
                    port = str(tds[2].string).strip()
                    print(ip + ": " + port)
                    yield ':'.join([ip, port])

            time.sleep(1)

# if __name__ == '__main__':
#     crawler = Crawler()
#     ids = crawler.crawl_xicidaili()
#     for id in ids:
#         print(id)
