# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    collection = 'products'

    image = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    shop = scrapy.Field()
    location = scrapy.Field()
