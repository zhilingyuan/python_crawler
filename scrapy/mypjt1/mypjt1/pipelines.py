# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class Mypjt1Pipeline(object):
    def __init__(self):
        self.file=codecs.open('.txt','wb',encoding='utf-8')
        import json
        '''同上
        '''
    def process_item(self, item, spider):
        '''
        i=json.dumps(dict(item)) #dict item 转换成字典
        '''
        l=str(item)+'\n'
        print(l)
        self.file.write(l)
        return item
    def close_spider(self,spider):
        self.file.close()






#setting
#ITEM_PIPLINES={'mypjt.pipelines.MypjtPipline':300}
