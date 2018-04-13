# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import re
import numpy as np
import datetime
from ippool.items import IppoolItem
import random

class IppraseSpider(scrapy.Spider):
    name = 'ipprase'
    allowed_domains = ['xicidaili.com']
    url_main=['http://www.xicidaili.com']
    page=20
    url=[]
    for _ in range(page):
        url_page=url_main[0]+"/nn/{}".format(_+1)
        url.append(url_page)
    start_urls=url
    #def start_requsets(self):
    	#for i in range(2,10):
    		#yield Request("http://www.xicidaili.com/nn/{}".html.format(i),
    			#callback=self.parse)
    #只调用了一次，这样使用出错
    #start_urls = ['http://www.xicidaili.com/nn/1','http://www.xicidaili.com/nn/2']
    #start_urls = ['http://www.xicidaili.com/nn/1']
    def parse(self, response):
    	ips = re.findall('<td>(\d+\.\d+\.\d+\.\d+)</td>', response.text)
    	ports = re.findall('<td>(\d+)</td>', response.text)
    	types = re.findall('<td class="country">([^<]+)</td>', response.text)
    	protocols = re.findall('<td>(HTTPS?)</td>', response.text)
    	speed_and_time=re.findall('<div title=\"(\d+\.\d+)秒\" class=\"bar\"',response.text)
    	speed_and_time=np.array(speed_and_time)
    	speed_and_time=speed_and_time.reshape((-1,2))
    	speeds=speed_and_time[:,0].tolist()
    	times=speed_and_time[:,1].tolist()
        #today=datetime.date.today()
        #today=today.strftime('%Y-%m-%d')
        #page_now=re.findall('<em class="current">(\d)</em>',response.text)
        #next_url=allowed_domains[0]+'/nn/{}'.format(page_now+1)
    	#from scrapy.shell import inspect_response
    	#inspect_response(response,self)	
    	for ip, port, _type, protocol,speed,time in zip(ips, ports, types, protocols,speeds,times):
            yield IppoolItem({
        	'website': 'xicidaili',
                'ip': ip,
                'protocol': protocol,
                'port': port,
                'types': _type,
                'speed':float(speed),
                'time':float(time),
                'rand_value':random.random()
                #'date':today,
            })

       
        #if page_now<page:
        #    yield Request(next_url,callback=self.parse)
        #else:
        #    pass
