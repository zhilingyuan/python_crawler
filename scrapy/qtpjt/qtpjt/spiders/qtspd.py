# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/tb']

    def parse(self, response):
        item=QtpjtItem()
        paturl=
        pass
