# -*- coding: utf-8 -*-
import scrapy


class IppraseSpider(scrapy.Spider):
    name = 'ipprase'
    allowed_domains = ['66ip.com']
    start_urls = ['http://66ip.com/']

    def parse(self, response):
        pass
