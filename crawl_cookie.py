#cookie jar
import urllib.request
import urllib.parse
import http.cookiejar
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q'
postdata=urllib.parse.urlencode({
    'username':'weisuen',
    'password':'aA123456'}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/28.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
               )
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()
with open('4.html','wb') as f:
    f.write(data)
