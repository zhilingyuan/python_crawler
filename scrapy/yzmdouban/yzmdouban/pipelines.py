# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import os
import datetime
class YzmdoubanPipeline(object):
    def process_item(self, item, spider):
    	this_url=item["pic_url"]
    	local_path="d:\yzmdouban"
    	if os.path.exists(local_path):
    		pass
    	else:
    		os.mkdir(local_path)
    	pic_name=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    	pic_path=local_path+'\\'+pic_name+'.jpg'
    	urllib.request.urlretrieve(this_url,pic_path)
    	return(item)