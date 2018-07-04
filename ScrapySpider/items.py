# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EhentaiPageItem(scrapy.Item):
    pagenumber=scrapy.Field()
    url=scrapy.Field()
    booknumber=scrapy.Field()

class EhentaiBookItem(scrapy.Item):
    booknumber=scrapy.Field()
    url=scrapy.Field()
    tag=scrapy.Field()
    title=scrapy.Field()
