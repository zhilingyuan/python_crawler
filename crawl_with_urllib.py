# without require package
# using urllib
# builtwith package try
# beutifulsoup 和 lxml,html parser 一样是一个解析库
# 是否使用依据个人
import builtwith
import urllib
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
print(builtwith.parse('http://www.baidu.com'))
url='http://www.baidu.com'
file=urllib.request.urlopen(url)
file_read=file.read()
filename1='baidu.html'
with open(filename1,'wb') as fw:
    fw.write(file_read)
s = BeautifulSoup(file)#？？？？
print(file.info())
print(file.getcode())
print(file.geturl())

#url 标准只允许一部分ASCII字符数字字母等部分符号
#对于不符的字符 进行编码
encodsina=urllib.request.quote('http://www.sina.com.cn')
print(encodsina)
decodsina=urllib.request.unquote(encodsina)
html = urllib.request.urlopen("http://www.pythonscraping.com")
# 这里使用bs 获取html结果与上面不同
bsObj = BeautifulSoup(html,'html5lib')
# 模拟浏览器的方法
# 1 add_header()修改报头
url='http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers1='User-Agent'
headers2='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
req=urllib.request.Request(url)
req.add_header(headers1,headers2)
data=urllib.request.urlopen(req).read()
filename2='blog.html'
with open(filename2,'wb') as fb:
    fb.write(data)
# 2 build_opener()修改报头
opener=urllib.request.build_opener()
opener.addheaders=[(headers1,headers2)]
data=opener.open(url).read()
filename3='blog2.html'
with open(filename3,'wb') as fb:
    fb.write(data)


