#crawl the image
import re
import urllib.request
page=1
url='https://list.jd.com/list.html?cat=670%2C671%2C672&go=0'
html=urllib.request.urlopen(url).read()
html=str(html)
pattern='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
imagelist=re.compile(pattern).findall(html)
num=1
for imageurl in imagelist:
    imageurl='http://'+imageurl
    imagename=str(num)+'.jpg'
    try:
        urllib.request.urlretrieve(imageurl,filename=imagename)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            num=num+1
        if hasattr(e,'reason'):
            num=num+1
    num=num+1
