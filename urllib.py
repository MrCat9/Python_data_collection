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
#












































































































