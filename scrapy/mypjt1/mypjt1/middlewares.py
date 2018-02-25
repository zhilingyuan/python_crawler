#IP池设置
#IPPOOL=[
#    {'ipaddr':'121.33.226.167:3128'},
#    {'ipaddr':'121.33.226.167:3128'}] 在settings.py中添加上面的ip池

#随机选择IP池中的IP
import random
from myfirstpjt.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip=ip
    def process_request(self,request,spider):
        thisip=random.choice(IPPOOL)
        print('IP is'+thisip['ipaddr'])
        request.meta['proxy']='http://'+thisip['ipaddr']
#setting
##DOWNLOADER_MIDDLEWARES={
        ##'myfirstpjt.middlewares.MyCustomDownloaderMiddleware':543,
        #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
        #'myfirstpjt.middleware.IPPOOLS':125}


#setting user-agent
#UAPOOL={'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko)','...'}

