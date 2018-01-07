# without require package
# using urllib
# builtwith package try
import builtwith
import urllib
print(builtwith.parse('http://www.baidu.com'))
url='http://www.baidu.com'
html=urllib.request.urlopen(url)
print(html)
