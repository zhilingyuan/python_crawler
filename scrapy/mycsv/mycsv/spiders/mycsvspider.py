# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers=['name','sex','addr','email']
    delimiter=','
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i =MycsvItem()
        i['name']=row['name'].encode()
        i['sex']=row['sex'].encode()
        print('name is :')
        print(i['name'])
        print('sex is :')
        print(i['sex'])
        print('--------------')
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        return i
