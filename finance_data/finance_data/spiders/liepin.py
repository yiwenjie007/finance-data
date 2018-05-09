# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LiepinSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['www.liepin.com', 'passport.liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?init=1&imscid=R000000058&d_sfrom=search_fp_bar&key=%E9%87%91%E8%9E%8D']

    rules = (
        Rule(LinkExtractor(allow=r'www.liepin.com/zhaopin/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//ul[@class="sojob-list"]//h3/@title').extract_first()
        print(title)
