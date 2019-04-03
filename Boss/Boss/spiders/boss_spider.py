# -*- coding: utf-8 -*-
import scrapy


class BossSpiderSpider(scrapy.Spider):
    name = 'boss_spider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']

    def parse(self, response):
        pass
