from scrapy import Spider
from urllib.parse import quote
from scrapysplashtest.items import ProductItem
from scrapy_splash import SplashRequest
import re

script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#mainsrp-pager div.form> input').value=% d;document.querySelector('#mainsrp-pager div.form> span.btn.J_Submit').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""


# mainsrp-pager > div > div > div > div.form > input

class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'thw=cn; cna=GaXLFtB4e0gCAd9oGf6QD1IA; t=ffdd800ddf95154cbfeef3056d862761; cookie2=11c4049da74366be8e81ead4977ec458; v=0; _tb_token_=e56ee33b19ee; _samesite_flag_=true; lgc=%5Cu6A31%5Cu7A7A%5Cu796D1999; dnk=%5Cu6A31%5Cu7A7A%5Cu796D1999; tracknick=%5Cu6A31%5Cu7A7A%5Cu796D1999; tg=0; enc=eZ6tUEnDmRYwYgjNIywFXLKbvXqX1q8Gf8M8FcyFqH9xOrKsdzh9LdX8w%2BUBBKvd6n0KDXFaksSQcvLPkyoefw%3D%3D; tfstk=a#O5ZSb0KjcNcbBvc1yR4BlgJHraFC63SOecHYN6QGG0WbvaG0HCR/FlyVZQJCplePcOQR; mt=ci=6_1; hng=CN%7Czh-CN%7CCNY%7C156; unb=3405740509; uc3=nk2=sCNYKe15rTISDA%3D%3D&id2=UNQ3Gk5jIEzvkw%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dBxdzykuUhkE1zs1g%3D; csg=31cf436b; cookie17=UNQ3Gk5jIEzvkw%3D%3D; skt=198ec5c48e7e4587; existShop=MTU4MTY2MjA3Mw%3D%3D; uc4=nk4=0%40stsn2Bqi6vvvFF8SpNb%2FFr70EjaQ&id4=0%40UgP8J%2BdLbGZhSXM3vTiQphOIpBqg; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=991; _nk_=%5Cu6A31%5Cu7A7A%5Cu796D1999; cookie1=B0SuKWw4gtwChTZm1MCdNFZVIatlVkb7%2BBRy39xU%2B5k%3D; uc1=cookie14=UoTUO8YJzFRZKA%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; _uab_collina=158167788867692737336639; JSESSIONID=B3B9CF7D62B9E91AC2932B8E810F140C; isg=BNfX-vpoRWkQecHkBn61jHCWZkshHKt-dzFTQSkE86YNWPeaMew7zpV6vvjGq4P2; l=cBgwB7mlQU64eL8bBOCanurza77OSIRYYuPzaNbMi_5pE6Ts2WQOo7m2eF96VjWd91YB46VFKQp9-etkqp3KRkK-g3fP.',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        }
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute', headers=headers,
                                    args={'lua_source': script, 'page': page, 'wait': 7})

            def parse(self, response):
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
