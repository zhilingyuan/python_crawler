# POST proviede 表单(form)
#
import urllib.request
import urllib.parse
filename='form.html'
url='http://www.iqianyue.com/mypost/'
postdata=urllib.parse.urlencode({
    'name':'ceo@iqianyue.com',
    'pass':'aA123456'}).encode('utf-8')
req=urllib.request.Request(url,postdata)
headers1='User-Agent'
headers2='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
req.add_header(headers1,headers2)
data=urllib.request.urlopen(req).read()
with open(filename,'wb') as fn:
    fn.write(data)
