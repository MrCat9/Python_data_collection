#常见文档读取(TXT, PDF)



#读取TXT文档
urlopen()  --> 默认使用ASCII码解码
#读取PDF文档
pdfminer3k



#读取TXT文档
#以 https://en.wikipedia.org/robots.txt 为例
from urllib.request import urlopen
html = urlopen('https://en.wikipedia.org/robots.txt')  --> urlopen()默认使用ASCII码解码
print(html.read())  --> 所以.read()时使用ASCII码编码
#这样写会有乱码
#乱码原因：
'''
计算机只能处理0和1两个数字，所以想要处理文本，必须把文本
变成0和1这样的数字，最早的计算机使用八个0和1来表示一个字
节，所以最大能够表示的整数是255=11111111。如果想要表示
更大的数，就必须使用更多的字节。

由于计算机是由美国人发明的，所以最早只有127个字符被编写
进计算机，也就是常见的阿拉伯数字，字母大小写，以及键盘上
的符号。这个编码被称为ASCI |编码，比如大写的字母A的ASCII
编码为65，65这个数字再被转换成二进制01000001，就是计算
机所真正处理的东西。

那么很显然，ASCII编码没办法表示我们的中文，于是中国就制定
了自己的GB2312编码，并且兼容ASCII编码，那么问题就来了，
使用GB2312编码的文字; 慕课网三个字，假设编码分别是61、
62、63，那么在ASCII码表中可能是键盘上的@符号，或者是其
他东西。

Unicode编码几乎兼容所有文字，但是Unicode码需要多一倍的存储空间
ASCII码一个字符8位，Unicode码一个字符16位

一个字节=1byte=8位=Bit

所有出现了utf-8编码
字符    ASCII编码   UTF-8编码      Unicode编码
A       01000001   01000001    00000000 01000001

utf-8码在表示中文的时候用两个8位的空间

可以这样做：
文档用Unicode码编写，但存储到计算机的时候转化成了utf-8编码
从计算机打开的时候，又把文档转换成Unicode码
这样做的话，存储用utf-8可以节省空间。读取的时候用Unicode码又可以保证兼容

再如：
服务器的一个Unicode编码的文档，在发送之前先转换为utf-8编码。
这样可以节省网络带宽

Python3字符串默认使用Unicode编码，所以Python3支持多语言。
以Unicode表示的str通过encode()方法可以编码为指定的bytes
如果bytes使用ASCII编码，遇到ASCII码表没有的字符会以\x##
表示，此时只要使用'\x##'.decode('utf-8')就可以了。
'''

#修改代码如下：
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/robots.txt')

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

print(html.read().decode('utf8'))



#读取PDF文档
#pdfminer3k
#在cmd下：
#pip install pdfminer3k

#                         set_document()
#PDF文档-->分析器PDFParser<-------------->文档对象PDFDocument-->文档对象的初始化方法initialize()  -->
#                          set_parser()                      （该方法可以接受一个字符串，如果PDF文档有密码的话可以在字符串里写入密码）

#
#-->资源管理器PDFResourceManager + 参数分析器LAParams --> 聚合器PDFageAggregator --> 解释器PDFPageInterpreter
#

#                         process_page()                       get_pages()
#解释器PDFPageInterpreter ---------------> 文档对象PDFDocument -------------> PDF文档
#

#
# 聚合器PDFageAggregator --> 读取 get_result()
#



#读取PDF文档
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

#在package下粘贴pdf文档 A Compact and Embedded Balanced.pdf

# w     以写的方式打开
# a     以追加的模式打开（从EOF开始，必要时创建新文件）
# r+    以读写模式打开
# w+    以读写模式打开
# a+    以读写模式打开
# rb    以二进制读模式打开
# wb    以二进制写模式打开
# ab    以二进制追加模式打开
# rb+   以二进制读写模式打开
# wb+   以二进制读写模式打开
# ab+   以二进制读写模式打开

fp = open('A Compact and Embedded Balanced.pdf', 'rb')  #获取文档对象  #rb --> 以二进制读的模式打开
#若要读取网络上的PDF：
#from urllib.request import urlopen
#fp = urlopen('http://gk.xmu.edu.cn/_upload/article/files/8f/f0/03862022456bb3a0421b8be3223d/90eeb364-6195-4cd3-958b-5bcc0bb71b99.pdf')

parser = PDFParser(fp)  #创建一个与文档关联的解释器

doc = PDFDocument()  #PDF文档对象

parser.set_document(doc)  #连接解释器和文档对象
doc.set_parser(parser)    #连接解释器和文档对象

doc.initialize('')  #初始化文档  #因为文档没有密码，所以为空

resource = PDFResourceManager()  #创建PDF资源管理器

laparam = LAParams()  #参数分析器

device = PDFPageAggregator(resource, laparams=laparam)  #创建聚合器=资源管理器+参数分析器

interpreter = PDFPageInterpreter(resource, device)  #创建PDF页面解释器

for page in doc.get_pages():  #使用文档对象得到页面的集合
    interpreter.process_page(page)  #使用页面解释器来读取
    layout = device.get_result()  #使用聚合器来获得内容
    for out in layout:
        if hasattr(out, 'get_text'):  #判断out是否有get_text这个属性
            print(out.get_text())
