# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670%2C671%2C672&go=0']
    
    def parse(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        
        item=QtpjtItem()
        paturl='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)'
        item["picurl"]=re.compile(paturl).findall(str(response.body))
        item["picid"]=re.compile(paturl).findall(str(response.body))
        yield item#忘记这一句会使得item 为空
        for i in range(2,4):
            nexturl='https://list.jd.com/list.html?cat=670%2C671%2C672&go='+str(i)
            yield Request(nexturl,callback=self.parse)#为什么会为空 items
            
        
