# crawl the url
# http://xxx.yyy
import re
import urllib.request
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/28.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
url='http://blog.csdn.net/'
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
data=str(data)
pattern='(https?://[^\s)";]+\.(\w|/)*)'
link=re.compile(pattern).findall(data)
link=list(set(link))
