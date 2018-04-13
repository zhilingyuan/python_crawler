# -*- coding: utf-8 -*-
import scrapy
import re
from yzmdouban.items import YzmdoubanItem
class YzmparseSpider(scrapy.Spider):
    num_yzm=100
    name = 'yzmparse'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/resetpassword']*num_yzm

    def parse(self, response):
        pic_url=re.findall('<img id=\"captcha_image\" src="(.*?)"',response.text)
        item=YzmdoubanItem()
        item["pic_url"]=pic_url[0]
        yield item
        pass
