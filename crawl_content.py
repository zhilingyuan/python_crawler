# qiushi content
import urllib.request
import re
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/28.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
url='http://qiushibaike.com/8hr/page/2'
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode('utf-8')
userpat='target="_blank" title="(.*?)">'
contentpat='<div class="content">(.*?)</div>'
userlist=re.compile(userpat,re.S).findall(data)
contentlist=re.compile(contentpat,re.S).findall(data)
numx=1
for content in contentlist:
    content=content.replace('\n','')
    name='content'+str(numx)
    exec(name+'=content')
    numx+=1
numy=1
for user in userlist:
    name='content'+str(numy)
    print('user'+str(numy)+':'+user)
    print('content:')
    exec('print('+name+')')
    print('\n')
    numy+=1
