#using proxy
import urllib.request
url='http://www.baidu.com'
proxy_addr='202.75.210.45:7777'
proxy=urllib.request.ProxyHandler({'http':proxy_addr})
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode('utf-8')
