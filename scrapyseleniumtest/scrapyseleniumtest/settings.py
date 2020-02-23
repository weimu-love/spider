# -*- coding: utf-8 -*-

# Scrapy settings for scrapyseleniumtest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapyseleniumtest'

SPIDER_MODULES = ['scrapyseleniumtest.spiders']
NEWSPIDER_MODULE = 'scrapyseleniumtest.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapyseleniumtest (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'thw=cn; cna=GaXLFtB4e0gCAd9oGf6QD1IA; t=ffdd800ddf95154cbfeef3056d862761; '
              'cookie2=11c4049da74366be8e81ead4977ec458; v=0 _tb_token_=e56ee33b19ee; _samesite_flag_=true;'
              ' lgc=%5Cu6A31%5Cu7A7A%5Cu796D1999; dnk=%5Cu6A31%5Cu7A7A%5Cu796D1999; '
              'tracknick=%5Cu6A31%5Cu7A7A%5Cu796D1999; tg=0; '
              'enc=eZ6tUEnDmRYwYgjNIywFXLKbvXqX1q8Gf8M8FcyFqH9xOrKsdzh9LdX8w%2BUBBKvd6n0KDXFaksSQcvLPkyoefw%3D%3D; '
              'tfstk=a#O5ZSb0KjcNcbBvc1yR4BlgJHraFC63SOecHYN6QGG0WbvaG0HCR/FlyVZQJCplePcOQR; mt=ci=6_1;'
              ' hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=FA3275F4F9488F879E9115FAE7025EE6; unb=3405740509; '
              'uc3=nk2=sCNYKe15rTISDA%3D%3D&id2=UNQ3Gk5jIEzvkw%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dBxdzykuUhkE1zs1g%3D; csg=31cf436b; '
              'cookie17=UNQ3Gk5jIEzvkw%3D%3D; skt=198ec5c48e7e4587; existShop=MTU4MTY2MjA3Mw%3D%3D; uc4=nk4=0%40stsn2Bqi6vvvFF8SpNb%2FFr70EjaQ&id4=0%40UgP8J%2BdLbGZhSXM3vTiQphOIpBqg;'
              ' _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=991; _nk_=%5Cu6A31%5Cu7A7A%5Cu796D1999; cookie1=B0SuKWw4gtwChTZm1MCdNFZVIatlVkb7%2BBRy39xU%2B5k%3D;'
              ' uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTUO8YJy3GC5A%3D%3D&tag=8&lng=zh_CN; '
              'l=cBgwB7mlQU64eJoSBOfaourza77T0IRb4sVzaNbMiICPOi1p5d6NWZVrOe89CnhVp6skJ353T9A8BeYBq1qWfdW22j-la; isg=BO_vs2WJ7SCGa-kc7uYtVNiefgP5lEO2Lyk7GQF8Fd5lUA9SCGRwBvdK00DuDhsu',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'scrapyseleniumtest.middlewares.ScrapyseleniumtestSpiderMiddleware': 543,
    'scrapyseleniumtest.middlewares.SeleniumMiddleware': 543,
    'scrapyseleniumtest.middlewares.DelayedRequestsMiddleware': 333,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapyseleniumtest.middlewares.ScrapyseleniumtestDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapyseleniumtest.pipelines.ScrapyseleniumtestPipeline': 300,
    'scrapyseleniumtest.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

KEYWORDS = ['iPad']

MAX_PAGE = 100

MONGO_URI = 'localhost'

MONGO_DB = 'taobao'

SELENIUM_TIMEOUT = 20

# PHANTOMJS_SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
