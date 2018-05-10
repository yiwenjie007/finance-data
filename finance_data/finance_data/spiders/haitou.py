# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HaitouSpider(CrawlSpider):
    name = 'haitou'
    allowed_domains = ['xyzp.haitou.cc']
    start_urls = ['https://xyzp.haitou.cc/brand/industry-financial']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
            'finance_data.middlewares.MyProxyMiddleware': 545,
        }
    }

    rules = (
        Rule(LinkExtractor(allow=r'/article/\d+\.html'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a')),
    )

    def parse_item(self, response):
        print(response.url)
