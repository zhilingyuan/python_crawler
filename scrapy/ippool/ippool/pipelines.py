# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class IppoolPipeline(object):
    def process_item(self, item, spider):
    	connection=pymongo.MongoClient()
    	proxy_db=connection.proxy_db
    	xici_tb=proxy_db.xici_tb
    	xici_tb.insert_one(dict(item))
    	return item
   
