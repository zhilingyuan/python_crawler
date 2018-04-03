# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest#Request:yield request
#import matplotlib.pylot as plt
#import matplotlib.image as mping
#mping.imread(path)
#plt.imshow()
#plt.show()


#from PIL import Image
#im=Image.open(path)
#im.show()
#im=np,array(im)


#import cv2
#cv2.imread("path")
#cv2.namedWindow("window")
#cv2.imshow("window","name")
#cv2.destroyAllWindows()
class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}

    def start_requests(self):
        return [Request("https://accounts.douban.com/login",meta={"cookiejar":1},
                        callback=self.parse)]
    
    start_urls = ['http://douban.com/']
    
    def parse(self, response):
        
        captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()#这里开始使得时候用错了括弧
        '''
            xpath 规则
            nodeA/nodeB：nodeA为根节点，nodeA下的所有nodeB节点；等价于nodeB。

            //nodeB：所有nodeB节点，在R包xml2中（比如函数xml_find_all()），
            //nodeB搜索范围是整个文档，忽略当前节点；而.//nodeB搜索范围是当前节点之下。

            //nodeB[1]：所有nodeB节点的第一个；//nodeB[last()-1]：所有nodeB节点的倒数第二个；nodeA/nodeB[position()<3]:当前nodeA节点，其下所有nodeB子节点的前两个。

            /nodeA/*：nodeA为根节点，nodeA下的所有节点；/*/*/nodeC：所有拥有两个父节点的nodeC节点；//*：所有节点。

            //*[count(nodeD)=3]：含有3个nodeD子节点的节点；//*[count(*)=2]：含有任意2个子节点的节点。

            //*[name()='nodeB']：所有名称为“nodeB”的节点，等价于//nodeB；//*[starts-with(name(),'N')]：所有名称以“N”开头的节点；
            //*[contains(name(),'N')]：所有名称中含有“N”的节点；//*[string-length(name()) = 3]：所有名称的字符串长度等于3的节点。

            //nodeA | //nodeB：所有nodeA，以及nodeB的节点，多个搜索条件合并，搜索添加没有限制。
            pass

            //@attr1：所有拥有attr1的属性，注意：返回的不是节点，而是类此attr1=text1的属性；
            //node1/@attr1：所有node1带有的attr1属性；//nodeB[@attr1]：所有拥有“attr1”属性的nodeB节点；
            //nodeB[@attr1='test1']：所有拥有“attr1”属性为“test1”的nodeB节点；
            //nodeB[normalize-space(@attr1)='test1']：所有拥有attr1属性为“test1”（属性去除字符串前后空格，内部连续空格替换为一个空格）的nodeB节点。

            //node1[@*]：所有node1带有任意属性的节点；//node1[not(@*)]：所有node1不带属性的节点。

            //node1[TEST1][TEST2]：多个属性形选择可以首位相接，依次判断是否为真。TEST1和TEST2同时为真，返回选择结果。
            //nodeA[nodeB/@attr1='test1']：选择所有nodeA节点，这些nodeA节点拥有nodeB子节点且属性“attr1”为“test1”。
            //nodeC[@attr1='test1'][../nodeB/@attr2='test2']：选择所有拥有“attr1”为“test1”的nodeC节点，而且这些nodeC节点有属性“attr2”为“test2”的nodeB父亲节点

            /nodeA/nodeB[nodeC>5]：nodeA为根节点，nodeA下的nodeB节点，而且这些nodeB节点必须有nodeC子节点，并且nodeC子节点内容大于5。

            /nodeA/nodeB[nodeC>5]/nodeD：nodeA为根节点，nodeA下的nodeB节点，而且这些nodeB节点必须有nodeC子节点，并且nodeC子节点内容大于5。

            //nodeC[.=5]：所有nodeC节点，其内容等于5。使用.代替自身。

            //nodeC/node()：选择所有nodeC节点下的所有点，包括节点下内容和子节点（距离最近，不包括子节点的子节点）。
    
            //nodeC/text()：选择所有nodeC节点下的内容

            轴？？？
        '''
        
        if len(captcha)>0:
            print("此时有验证码")
            localpath="D:captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            print("人工识别验证码")
            import cv2
            img=cv2.read(localpath)
            cv2.namedWindow("image")
            cv2.imshow("image",img)
            cv2.waitKey(5)
            cv2.destroyAllWindows()
            captcha_value=input()
            data={
                "form_email":"1282449098@qq.com",
                "form_password":"yzlno1pass1",
                "captcha-solution":captcha_value,
                "redir":"https://www.douban.com/people/128735118/"
                }
           
        else:
        
            print("没有验证码")
            data={
                "form_email":"1282449098@qq.com",
                "form_password":"yzlno1pass1",
               # "captcha-solution":captcha_value,
                "redir":"https://www.douban.com/people/128735118/"
                }
        print("登陆中。。。")
        return [FormRequest.from_response(response,
                                               headers=self.header,
                                               formdata=data,
                                               callback=self.next)]
    def next(self,response):
        print("完成登陆")
        xtitle="/html/head/title/text()"
        xnotetitle="//div[@class='note-header p12']/a/@title"
        xnotetime="//div[@class='note-header p12']//span[@class='pl']/text()"
        xnotecontent="//div[@class='mbtr2']/div[class='note']/text()"
        xnoteurl="//div[@class='note-header p12']/a/@href"

        title=response.xpath(xtitle).extract()
        notetitle=response.xpath(xnotetitle).extract()
        notetime=response.xpath(xnotetime).extract()
        notecontent=response.xpath(xnotecontent).extract()
        noteurl=response.xpath(xnoteurl).extract()

        for i in range(0,len(notetitle)):
            
            print("第"+str(i+1)+"文章")
            print(notetitle[i])
            print(notetime[i])
            print(notecontent[i])
            print(noteurl[i])
            print('---------')
                    
                

        
        
            
