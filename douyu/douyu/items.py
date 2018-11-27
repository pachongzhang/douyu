# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    avatar = scrapy.Field()
    hn = scrapy.Field()
    nickname = scrapy.Field()
    rid = scrapy.Field()
    roomName = scrapy.Field()
    verticalSrc = scrapy.Field()
    pass