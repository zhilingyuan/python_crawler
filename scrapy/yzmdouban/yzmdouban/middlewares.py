# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import pymongo
import random
class YzmdoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        
        for r in start_requests:
            #随机
            '''
            cursor=xici_tb.find_one({"$and":[{'speed':{"$lt":0.5}},{'time':{"$lt":0.5}},{'rand_value':{'$lt':rand_index}}]})
            if(cursor):
                pass
            else:
                cursor=xici_tb.find_one({"$and":[{'speed':{"$lt":0.5}},{'time':{"$lt":0.5}},{'rand_value':{'$gt':rand_index}}]}) 
            proxy_ip=cursor['ip']
            proxy_port=cursor['port']
            proxy_protocol=cursor['protocol']
            proxy=proxy_protocol+'://'+proxy_ip+':'+proxy_port
            r.meta["proxy"]=proxy
            '''
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class YzmdoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        rand_index=random.random()
        connection=pymongo.MongoClient()
        proxy_db=connection.proxy_db
        xici_tb=proxy_db.xici_tb
        cursor=xici_tb.find_one({"$and":[{'speed':{"$lt":0.5}},{'time':{"$lt":0.5}},{'rand_value':{'$lt':rand_index}}]})
        if(cursor):
            pass
        else:
            cursor=xici_tb.find_one({"$and":[{'speed':{"$lt":0.5}},{'time':{"$lt":0.5}},{'rand_value':{'$gt':rand_index}}]}) 
        proxy_ip=cursor['ip']
        proxy_port=cursor['port']
        proxy_protocol=cursor['protocol']
        proxy=proxy_protocol+'://'+proxy_ip+':'+proxy_port
        request.meta["proxy"]=proxy
        print(proxy)
        

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
