#from bs4 import BeautifulSoup as bs  #这样写的话，下面要用BeautifulSoup时可以写bs
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())  #格式化输出

print()

print(soup.title)  #<title>The Dormouse's story</title>
print(soup.title.name)  #title
print(soup.title.string)  #The Dormouse's story  #输出title标签内的内容
#如果title标签内还有其他标签的话， print(soup.title.string) 将输出None， 这时候考虑用print(soup.title.get_text())
print(soup.title.parent.name)  #head  #输出title父类的名字

print(soup.p)  #<p class="title"><b>The Dormouse's story</b></p>  #获取p标签
print(soup.p['class'])  #['title']  #获取p标签class的名字

print(soup.a)  #<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>  #获取a标签

print(soup.find(id='link3'))  #<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
#获取id='link3'的标签

print(soup.find(id='link3').string)  #Tillie  #获取id='link3'的标签内的内容
print(soup.find(id='link3').get_text())  #Tillie  #获取id='link3'的标签内的内容

print(soup.find_all('a'))  #[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#以列表形式返回所有的a标签
print(soup.findAll('a'))  #[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for link in soup.findAll('a'):  #获取所有a标签内的内容
    print(link.string)
#Elsie
#Lacie
#Tillie

print(soup.find('p', {'class':'story'}))
"""
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
"""
print(soup.find('p', {'class':'story'}).string)  #None
print(soup.find('p', {'class':'story'}).get_text())
"""
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
"""

import re
for tag in soup.find_all(re.compile('^b')):  #以b开头  #find_all方法接收一个字符串
    print(tag.name)
'''
body
b
'''

data = soup.findAll('a', href=re.compile(r'^http://example.com/'))  #在a标签中查找 href="http://example.com/ 开头的
print(data)  #[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#但这样写也能够匹配出  <a class="sister" href="http://exampleScom/elsie" id="link1">Elsie</a>  #因为.代表任意
#所以应该改写成：
data = soup.findAll('a', href=re.compile(r'^http://example\.com/'))
print(data)
#或者改成：
data = soup.findAll('a', href=re.compile(r'^http://example[.]com/'))
print(data)
