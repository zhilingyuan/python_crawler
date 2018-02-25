#agent 池
##setting user-agent
#UAPOOL={'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko)','...'}


import random
from myfirstpjt.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import UserProxyMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.ua=ua
    def process_request(self,request,spider):
        thisua=random.choice(UAPOOL)
        print('this user-agent is '+thisua)
        request.headers.setdefault('User-Agent',thisua)

#Enable or disable downloader middlewares
#
#DOWNLOADER_mIDDLEWARES={
###          'myfirstpjt.middlewares.MyCustomDownloaderMiddleware':543,
            #scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':2,
#            'myfirstpjt.uamid.Uamid':1
#}
