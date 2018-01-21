#urllib.error
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blg.csdn.net")
except urllib.error.URLError as e:
    #import pdb
    #pdb.set_trace()
    print(e.args)
except urllib.error.HTTPError as e:
    print(e.args)
