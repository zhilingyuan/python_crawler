#ipconfig /displaydns
import re
import urllib.request
import time
import urllib.error

def use_proxy(proxy_addr,url):
    try:
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        #opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        #urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)

    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

def getlisturl(key,pagestart,pageend,proxy):
    listurl=[]
    try:
        page=pagestart
        keycode=urllib.request.quote(key)
        pagecode=urllib.request.quote("&page=")
        for page in range(pagestart,pageend+1):
            url="http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            data1=use_proxy(proxy,url)
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print('get url'+str(len(listurl))+'page')
        return listurl 
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)

    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

def getcontent(listurl,proxy):
    i=0
    html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "HTTP://
www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<title>微信文章</title>
</head>
<body>'''
    with open('6.html','wb') as fh:
        fh.write(html1.encode('utf-8'))
    with open('6.html','ab') as fh:
        for i in range(0,len(listurl)):
            for j in range(0,len(listurl[i])):
                try:
                    url=listurl[i][j]
                    url=url.replace("amp;","")
                    data=use_proxy(proxy,url)
                    titlepat='<title>(.*?)</title>'
                    title=re.compile(titlepat).findall(data)
                    contentpat='id="js_content">(.*?)id="js_sg_bar"'
                    content=re.compile(contentpat,re.S).findall(data)
                    thistitle='未获取'
                    thiscontent='未获取'
                    if(title!=[]):
                        thistitle=title[0]
                    if(content!=[]):
                        thiscontent=content[0]
                    dataall="<p>标题为："+thistitle+"</p><p>内容为:"+thiscontent+"</p><br>"
                    fh.write(dataall.encode('utf-8'))
                    print(str(i)+'页'+str(j)+'项')
                except urllib.error.URLError as e:
                    if hasattr(e,"code"):
                        print(e.code)
                    if hasattr(e,"reason"):
                        print(e.reason)
                        time.sleep(10)
                except Exception as e:
                    print("exception:"+str(e))
                    time.sleep(1)
        html2='''</body>
</html>
'''
        fh.write(html2.encode('utf-8'))
        fh.close()
if __name__=='__main__':
    headers=("User-Agent",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    #listurl=[]
    key='魔法'
    proxy='119.6.136.1222:80'
    proxy2=''
    pagestart=1
    pageend=2
    listurl=getlisturl(key,pagestart,pageend,proxy)
    getcontent(listurl,proxy)
    
        
            
            
