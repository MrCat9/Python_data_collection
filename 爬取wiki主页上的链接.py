#获得维基百科主页中所有的词条信息
#右键-->检查-->network-->刷新-->doc-->main_page
Request URL:https://en.wikipedia.org/wiki/Main_Page
Request Method:GET
Status Code:304 
Remote Address:[2620:0:863:ed1a::1]:443
Referrer Policy:unsafe-url

#词条链接:
<a href="/wiki/Hurricane_Marie_(2014)" title="Hurricane Marie (2014)">Hurricane Marie</a>
<a href="/wiki/Interior_with_Young_Woman_Seen_from_the_Back" title="Interior with Young Woman Seen from the Back">Interior with Young Woman Seen from the Back</a>



#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf8')  #请求URL，并把结果同UTF-8编码
soup = BeautifulSoup(resp, 'html.parser')  #用BeautifulSoup解析
#print(soup)

listUrls = soup.findAll('a', href=re.compile(r'^/wiki/'))  #获取所有以 /wiki/ 开头的a标签的href属性
#print(listUrls)
for url in listUrls:  #输出所有的词条对应的名称和URL
    if not re.search(r'.(jpg|JPG)$', url['href']):  #过滤图片（以.jpg或者.JPG结尾的URL）
        print(url.get_text(),'<--->','https://en.wikipedia.org'+url['href'])  #输出URL的文字和对应的链接
                 #这里用string也行
                 #string只能获取一个，get_text()可以获取标签下所有的文字
