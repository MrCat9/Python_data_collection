#测试python，urllib安装成功：
#在cmd下
#python  #验证python安装成功
#from urllib.request import urlopen  #验证urllib安装成功

#安装beautifulsoup4：
#在cmd下：
#pip install beautifulsoup4

#验证beautifulsoup4安装成功:
#在cmd下：
#python
#from bs4 import BeautifulSoup



#urllib的用法
#urllib是python3.x 中提供的一系列操作URL的库，
#它可以轻松的模拟用户使用浏览器访问网页



#
print('a' == '\u0061')  #True  
#在python3里,字符就是unicode字符，字符串就是unicode字符数组
#str转bytes叫encode，bytes转str叫decode
#



from urllib import request  #导入urllib库的request模块
resp = request.urlopen('http://www.baidu.com')  #请求URL
htmlBytes = resp.read()  #使用相应对象输出数据
print(htmlBytes.decode('utf-8'))
#报错：UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 211663: illegal multibyte sequence
#修改：把python的默认编码改成'utf-8'就不会报错，但是中文显示会有乱码，所以改成'gb18030'
from urllib import request

import io  
import sys  

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  #改变标准输出的默认编码  

resp = request.urlopen('http://www.baidu.com')
print(resp)  #<http.client.HTTPResponse object at 0x000002216CEA4D68>
htmlBytes = resp.read()
print(htmlBytes)
print(htmlBytes.decode('utf-8'))

#一些常用的和中文有关的编码的名称，分别赋值给encoding，就可以看到不同的效果了：
编码名称     用途
utf8        所有语言
gbk         简体中文
gb2312      简体中文
gb18030     简体中文
big5        繁体中文
big5hkscs   繁体中文



#查看浏览器的头:
#chrome下：
#右键-->检查-->network-->刷新一下-->doc-->Name-->www.baidu.com-->headers
#-->User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
#               浏览器        操作系统                                                            浏览器版本

#模拟真实浏览器
#携带User-Agent头
from urllib import request

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  #改变标准输出的默认编码

url = 'https://www.baidu.com'
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))



#使用post
from urllib import parse  #导入urllib库下面的parse
postData = parse.urlencode([  #使用urlencode生成post数据  #列表，列表里面是元组
    (key1, val1),
    (key2, val2),
    (keyn, valn),
    ])
request.urlopen(req, data = postData.encode('utf_8'))  #使用postData发送post请求
resp.status  #得到请求状态
resp.reason  #得到服务器类型



#使用urllib发送post请求
#http://www.thsrc.com.tw/index.html  -->  右键，检查  -->  Network  -->Doc
#选择  2018/03/15 14：00 从台北站出发，到台南站  进行测试  -->  点击查询
#在doc下可以看到SearchResult
#SearchResult  -->  Headers
#结果如下：
Request URL:http://www.thsrc.com.tw/tw/TimeTable/SearchResult
Request Method:POST
Status Code:200 OK  -->响应结果
Remote Address:61.31.57.189:80  -->地址
Referrer Policy:no-referrer-when-downgrade
Cache-Control:private
Content-Length:100124
Content-Type:text/html; charset=utf-8
Date:Thu, 15 Mar 2018 06:00:05 GMT
Set-Cookie:TS01ce71a1=013b146f10f3c671dd1fd8ccd6279f888cac51569120e776622b365353d7269923fd19a9425e2eb3c5385666837b1cdff96c180320; Path=/
X-AspNet-Version:2.0.50727
X-AspNetMvc-Version:2.0
X-Frame-Options:SAMEORIGIN
X-Powered-By:ASP.NET
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:172
Content-Type:application/x-www-form-urlencoded
Cookie:ASP.NET_SessionId=dssg0mry0cvwlvali2lgrb45; TS01ce71a1=013b146f104dcb1fc3cdff4722cedb4ccd97c20d7b5b4058f1d01b981170e83a560ece8f7ee9bd2f29af6dbca30161ea4abe66321f; __utma=214205650.707996810.1521093232.1521093232.1521093232.1; __utmc=214205650; __utmz=214205650.1521093232.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=214205650.1.10.1521093232
Host:www.thsrc.com.tw
Origin:http://www.thsrc.com.tw  -->来源
Referer:http://www.thsrc.com.tw/index.html
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36  -->浏览器
StartStation:977abb69-413a-4ccf-a109-0272c24fd490  -->post请求的内容
EndStation:9c5ac6ca-ec89-48f8-aab0-41b738cb1814  -->post请求的内容
SearchDate:2018/03/15  -->post请求的内容
SearchTime:14:00  -->post请求的内容
SearchWay:DepartureInMandarin  -->post请求的内容

#要伪装爬虫一般需要 Origin 和 User-Agent



#使用urllib发送post请求
from urllib.request import Request, urlopen
from urllib import parse

req = Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')

postData = parse.urlencode([
    ('StartStation','977abb69-413a-4ccf-a109-0272c24fd490'),
    ('EndStation','9c5ac6ca-ec89-48f8-aab0-41b738cb1814'),
    ('SearchDate','2018/03/15'),
    ('SearchTime','14:00'),
    ('SearchWay','DepartureInMandarin'),
    ])

req.add_header('Origin', 'http://www.thsrc.com.tw')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')

resp = urlopen(req, data = postData.encode('utf8'))

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

print(resp.read().decode('utf8'))
