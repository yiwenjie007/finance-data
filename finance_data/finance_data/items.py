# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinanceDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HaitouItem(scrapy.Item):
    company = scrapy.Field()
    start_time = scrapy.Field()
    position = scrapy.Field()
    city = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
