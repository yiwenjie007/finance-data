# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from finance_data.items import HaitouItem
from w3lib.html import remove_tags


class HaitouSpider(CrawlSpider):
    name = 'haitou'
    allowed_domains = ['xyzp.haitou.cc']
    start_urls = ['https://xyzp.haitou.cc/brand/industry-financial']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
            'finance_data.middlewares.MyProxyMiddleware': 545,
        },
        'ITEM_PIPELINES':{
            'finance_data.pipelines.HaiTouPipeline': 301
        }
    }

    rules = (
        Rule(LinkExtractor(allow=r'/article/\d+\.html'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a')),
    )

    def parse_item(self, response):
        company = response.xpath('//div[@class="article-header"]/div[@class="article-logo"]/img/@alt').extract_first()
        start_time = remove_tags(response.xpath('//div[@class="article-info"]//div[contains(@class, "post-time")]//span').extract()[1])
        position = remove_tags(','.join(response.xpath('//div[@class="position-item"]/span/text()').extract()))
        city = remove_tags(','.join(response.xpath('//div[@class="article-info"]//div[contains(@class, "cities")]//span').extract()[1:]))
        tag = remove_tags(','.join(response.xpath('//div[@class="article-info"]//div[contains(@class, "tags")]//span').extract()[1:]))
        url = response.url
        item = HaitouItem()
        item['company'] = company
        item['start_time'] = start_time
        item['position'] = position
        item['city'] = city
        item['tag'] = tag
        item['url'] = url
        yield item
