# -*- coding: utf-8 -*-
import scrapy
from mypjt1.items import url_detail

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']
    start_urls = ('http://slide.news.sina.com.cn/slide_1_86058_240033.html',
                  'http://slide.news.sina.com.cn/slide_1_86058_240043.html',
                  'http://news.sina.com.cn/china/xlxw/2018-02-08/doc-ifyrkuxs2241755.shtml')
    

    def parse(self, response):
        item=url_detail()
        item['urlname']=response.xpath('/html/head/title/text()')
        print(item['urlname'])
   
    def __init__(self,myurl=None,*args,**kwargs):#重载init 外部参数运行 类似 c++
        super(WeisuenSpider,self).__init__(*args,**kwargs)
        print('urls crawlled are %s'%myurl)
        self.start_urls=['%s'%myurl]
