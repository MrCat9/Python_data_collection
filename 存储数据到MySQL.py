#  pip install pymysql  -->安装pymysql

# http://github.com/PyMySQL/PyMySQL



#
import pymysql  #导入开发包

connection = pymysql.connect(  #获取数据库链接
    host='localhost',
    user='root',
    passwd='123456',
    db='pymysql_test01',
    charset='uft8mb4'  #编码
    )

cursor = connection.cursor()  #获取会话指针
cursor.execute(sql, (参数1, 参数n))  #执行sql语句

connection.commit()  #提交
connection.close()  #关闭



#
在数据库中新建table
field name    datatype    len   not null?   auto incr?
id            int         11       √            √
urlname       varchar     255      √
urlhref       varchar     1000     √

创建的表格如下
id    urlname   urlhref



#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf8')
soup = BeautifulSoup(resp, 'html.parser')
#print(soup)

listUrls = soup.findAll('a', href=re.compile(r'^/wiki/'))
#print(listUrls)
for url in listUrls:
    if not re.search(r'.(jpg|JPG)$', url['href']):  
        print(url.get_text(),'<--->','https://en.wikipedia.org'+url['href'])

        connection = pymysql.connect(  #获取数据库链接
            host='localhost',
            user='root',
            passwd='123456',
            db='pymysql_test01',
            charset='utf8mb4'  #编码
            )

        try:
            with connection.cursor() as cursor:  #获取会话指针
                sql = 'insert into `urls`(`urlname`,`urlhref`) values(%s, %s)'  #创建sql语句
                cursor.execute(sql, (url.get_text(),'https://en.wikipedia.org'+url['href']))  #执行sql语句
                 
                connection.commit()  #提交
        finally:
            cursor.close()
            connection.close()

#try块里面也可以写成：
#         try:
#             cursor = connection.cursor()
#             sql = 'insert into `urls`(`urlname`,`urlhref`) values(%s, %s)'
#             cursor.execute(sql, (url.get_text(),'https://en.wikipedia.org'+url['href']))
#                  
#             connection.commit()
#         finally:
#             cursor.close()
#             connection.close()
