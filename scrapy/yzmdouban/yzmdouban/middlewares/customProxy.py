
import random
import pymongo

class RandomProxy(object):
    def process_request(self,request, spider):
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