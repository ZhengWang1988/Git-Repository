# 如何在列表,字典,集合中根据条件筛选数据
from random import randint
data = [randint(-10,10) for _ in range(10)]
filter(lambda x:x >= 0, data)
[for x in data if x >= 0]

timeit filter(lambda x:x >= 0, data) #测试该步骤运行耗时


d = {x:randint(60,100) for x in range(1,21)} #学号:成绩
{k:v for k,v in d.iteritems() if v >= 90}

s = set(data)
{for x in s if x % 3 == 0}

# 如何为元组中的每个元素命名,提高程序可读性
students = ('Jim',22,'male','Jim@mail.com')
NAME,AGE,SEX,EMAIL = range(4)
print(students[NAME])
print(students[AGE])

from collections import namedtuple
namedtuple('Students',['name','age','sex','email'])
s1 = Students('Jim',22,'male','Jim@mail.com')
s2 = Students(name='Jim',age=22,sex='male',email='Jim@mail.com')
print(s1.name)

# 如何统计序列中元素出现的频度
from random import randint
data = [randint(0,20) for _ in range(30)]
c = dict.fromkeys(data,0)
for x in data:
	c[x] += 1

from collections import Counter
c2 = Counter(data)
c2.most_common(3) #出现频度最高的前三个

# 筛选文章中单词出现频度最高的前十
import re
txt = open(filename).read()
c3 = Counter(re.split('\W+', txt))
c3.most_common(10)

# 如何根据字典中值的大小,对字典中的项排序
from random import randint
dicts = {k:randint(60,100) for k in 'abcdefg'}
# zip(dicts.values(),dicts.keys())
sorted(zip(dicts.itervalues(),dicts.iterkeys()))
sorted(dicts.items(),key=lambda x:x[1])  #把每一个元组传入sorted函数,并设置key为元组第二个值

# 如何快速找到多个字典中的公共键(key)
from random import randint,sample
sample('abcdefg', randint(3,6))  #随机从中取3--6个字符
s1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}

res = []
for k in s1:
	if k in s2 and k in s3:
		res.append(k)

s1.viewkeys & s2.viewkeys & s3.viewkeys  #三个字典的公共键的集合

map(dict.viewkeys,[s1,s2,s3]) #由字典的键组成的列表
reduce(lambda a,b:a & b,map(dict.viewkeys,[s1,s2,s3]))

# 如何让字典保持有序?
from collections import OrderedDict
d = OrderedDict()
d['Jim'] = (1,24)
d['Lily'] = (2,27)
d['Leo'] = (3,31)
for k in d:
	print(k)

=================================================
from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFGH')
start = time()
for i in range(8):
	input()
	p = players.pop(randint(0,7 - i))
	end = time()
	print(i+1,p,end-start)
	d[p] = (i+1,end-start)
print()
print('-'*30)
for k in d:
	print(k,d[k])
=================================================
# 如何实现用户的历史记录功能(最多N条)
from collections import deque

N = randint(0,100)
history = deque([], 5)	#长度为5的列表,遵循先进先出的原则
def guess(k):
	if k == N:
		print('right')
		return True
	if k < N:
		print('less than N')
	else:
		print('greater than N')
	return False

while True:
	line = input('please input a number:')
	if line.isdigit():
		k = int(line)
		history.append(k)
		if guess(k):
			break
	elif line == 'history' or line == 'h?':
		print(list(history))

import pickle
# pickle可以将队列(python对象)存入文件,再次运行程序时将其导入
pickle.dump(obj,open('history_file',w))
pickle.load(open('history_file'))



# 如何实现可迭代对象和迭代器对象
# 列表,字符串均为可迭代对象,可实现__iter__方法
lists = [1,2,3,4,5,6]	#可迭代对象
iter(lists)	#迭代器对象
=================================================
import requests
def getWeather(city):
	r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
	data = r.json()['data']['forecast'][0]
	return '%s : %s, %s ' % (city,data['low'],data['high'])
print(getWeather('北京'))
print(getWeather('上海'))

from collections import Iterable,Iterator
# 实现迭代器对象
class WeatherIterrator(Iterator):
	def __init__(self,cities):
		self.cities = cities
		self.index = 0
	def getWeather(self,city):
		r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		data = r.json()['data']['forecast'][0]
		return '%s : %s, %s ' % (city,data['low'],data['high'])
	def next(self):
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]:
		self.index += 1
		return self.getWeather(city)

# 实现可迭代对象
class WeatherIterable(Iterable):
	def __init__(self,cities):
		self.cities = cities
	def __iter__(self):
		return WeatherIterrator(self.cities)
=================================================

# 如何使用生成器函数实现可迭代对象
class PrimeNumber:
	def __init__(self,start,end):
		self.start = start
		self.end = end
	def isPrime(self,k):	#判断传入的参数是否是素数
		if k < 2:
			return False

		for i in range(2,k):
			if k % i == 0:
				return False
		return True
	def __iter__(self):
		for k in range(self.start,self.end + 1):
			if self.isPrime(k):
				yield k 	#将这个范围内的所有值进行遍历,判断是否是素数,返回所有素数


# 如何进行反向迭代以及如何实现反向迭代
l = [1,2,3,4,5,6]
l.reverse() #会改变原列表
l[::-1]  #会生成新列表,浪费内存
reversed(l) #生成一个反向的迭代器

class FloatRange:
	def __init__(self,start,end,step=0.1):
		self.start = start
		self.end = end
		self.step = step
	def __iter__(self):
		t = self.start
		while t <= self.end:
			yield t
			t += self.step
	def __reversed__(self):
		t = self.end
		while t >= self.start:
			yield t
			t -= self.step

# 如何对迭代器做切片操作
from itertools import islice
f = open(filename,'r',encoding='utf-8')
s = islice(f, 10,30)  #生成一个迭代器(10行到30行)
islice(f,500)  #从开始到500行
islice(f,10,None)  #从第10行到最后


# 如何在一个for语句中迭代多个可迭代对象
from random import randint
yuwen = [randint(60,100) for _ in range(40)]  #生成语文成绩列表
shuxue = [randint(60,100) for _ in range(40)]
english = [randint(60,100) for _ in range(40)]
# 内置函数zip,能将多个可迭代对象合并,每次迭代返回一个元组
zip([1,2,3,4],['a','b','c','d'])	#[(1,'a'),(2'b),(3,'c'),(4,'d')]
for y,s,e in zip(yuwen,shuxue,english):
	total.append(y + s + e)
# 标准库中的itertools.chain,能将多个可迭代对象连接
from itertools import chain
c1 = [randint(60,100) for _ in range(38)]
c2 = [randint(60,100) for _ in range(45)]
c3 = [randint(60,100) for _ in range(40)]
c4 = [randint(60,100) for _ in range(42)]
count = 0
for s in chain(c1,c2,c3,c4):
	if s > 90:
		count += 1


# 如何拆分含有多种分隔符的字符串
# res = s.split(',')
# map(lambda x:x.split('.'),res)
def mySplit(s,ds):
	res = [s]
	for d in ds:
		t = []
		map(lambda x:t.extend(x.split(d)),res)
		res = t
	return [for x in res if x]	#过滤空字符串
s = r'a,b.c;d|e/fg/hij]kl(mn,opqr{stu,vw`xyz'
print(mySplit(s,',.;|/]({`\t'))

import re
re.split(r'[,.;|/]({`\t]+', s)

# 如何判断字符串a是否以字符串b开头或结尾?
import os,stat
os.listdir('.')	#列出当前目录下所有文件的列表
s = 'go.sh'
s.endswith(('.sh','.py'))	#判断s是以.sh或.py结尾
[name for name in os.listdir('.') if name.endswith(('.sh','.py'))]
os.stat('e.py')  #列出该文件的状态信息
# oct(os.stat('e.py').st_mode)	以八进制形式展示文件权限信息

# 如何调整字符串中文本的格式 2016-10-01 --> 10/01/2016
import re
log = open(filename).read()
re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)

# 如何将多个小字符串拼接成一个大的字符串
lists = ['ab','cd','ef','gh','hi','jk']
s = ''
for i in lists:
    s += i
# (内存开销较大,不建议使用)
''.join(lists)  <推荐使用该方法>
list2 = ['ab','cd',123,45]
''.join((str(x) for x in list2))  #生成器方式进行join拼接

# 如何对字符串进行左,右,居中对齐?
s = 'abc'
s.ljust(20)
s.ljust(20, '=')
s.rjust(20)
s.center(30)

format(s,'<20')
format(s,'>20')
format(s,'^20')

d = {'apple':200,'google':350,'facebook':165,'Android OS':124}
m = max(map(len,d.keys()))	#取各个键的最大长度
for k in d:
	print(k.ljust(m),':',d[k])


# 如何去掉字符串中不需要的字符
s = '  abc  123  '
s.strip()  #去掉两头的空白字符
s.lstrip() #去掉左边的空白
s.rstrip() #去掉右边的空白
s = '+++abc---'
s.strip('+-')  #去掉'+' 和'-'

s = 'abc:123'
s[:3] + s[4:]

s = '\tabc\txyz'
s.replace('\t', '')

s = '\r\tabc\t\rbvc\n'
import re
re.sub('[\t\r\n]', '', s)

s = 'abc1234567xyz'
import string
string.maketrans('abcxyz','xyzabc')  #制造字符的映射关系 a映射x b映射y
s.translate(string.maketrans('abcxyz','xyzabc'))  
# xyz1234567abc


# 如何读写文本文件
f = open('py3.txt','wt',encoding='utf-8')
f.write('你好')
f.close()
f = open('py3.txt','rt',encoding='utf-8')
print(f.read())

# 如何处理二进制文件
f = open('demo.wav','rb')
info = f.read(44)
import struct
struct.unpack('h', info[22:24])  #音频文件声道数
struct.unpack('i', info[4:28])   #采样频率

import array
n = (f.tell() - 44) / 2
buf = array.array('h', (0 for _ in range(n)))
f.seed(44)  #文件指针指向数据部分
f.readinto(buf)  #将数据读入buf中
# open函数想以二进制模式打开文件,指定mode参数为'b'
# 二进制数据可以用readinto,读入到提前分配好的buffer中,便于数据处理
# 解析二进制数据可以使用标准库中的struct模块的unpack方法


# 如何设置文件的缓冲
全缓冲:
# 普通文件默认的缓冲区是4096个字节
f = open('demo.txt','w',buffering=2048)
f.write('a'*1024)  #tail实时查看文件无显示内容
f.write('b'*1024)  #依然无内容显示
f.write('c')   #文件写入内容超出缓冲区设置大小,文本内容显示出来
行缓冲:
f = open('demo2.txt','w',buffering=1)
f.write('abc')
f.write('\n')
f.write('xyz\n')
无缓冲:
f = open('demo2.txt','w',buffering=0)
f.write('123')


# 如何将文件映射到内存
1.在访问某些二进制文件时,希望能把文件映射到内存中,可以实现随机访问. (framebuffer设备文件)

2.某些嵌入式设备,寄存器被编址到内训地址空间,我们可以映射/dev/mem某范围,去访问这些寄存器

3.如果多个进程映射同一个文件,还能实现进程通信的目的.


# 如何使用临时文件?
from tempfile import TemporaryFile,NamedTemporaryFile
f = TemporaryFile()  #创建一个临时文件对象
f.write('hello,world' * 10000)	#向临时文件写入临时数据
f.seek(0)	#文件指针指向临时文件头部
f.read(100)   #读取数据
# 系统中找不到该文件,只能有该临时文件的对象来访问

ntf = NamedTemporaryFile()
print(ntf.name)
# 系统中临时文件目录中可以找到该临时文件,创建新的临时文件时之前的会被删除,可设置默认参数delete=False来保存之前的临时文件


# 如何读写csv数据?
from urllib import urlretrieve
urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz','pingan.csv')
import csv
rf = open('pingan.csv','rb')
reader = csv.reader(rf)
header = (reader.next())  #逐行打印

wf = open('pingan.csv','wb')
writer = csv.writer(wf)
writer.writerow(header)		#写入头部
writer.writerow(reader.next())
wf.flush()   #保存到文件中
================================================
import csv
with open('pingan.csv','rb') as rf:
	reader = csv.reader(rf)
	with open('pingan2.csv','wb') as wf:
		writer = csv.writer(wf)
		headers = reader.next()
		writer.writerow(headers)
		for row in reader:
			if row[0] < '2016-01-01':
				break
			if int(row[5]) >= 50000000:
				writer.writerow(row)
print('writing end')
================================================

# 如何读写json数据
# json.dumps() 和 json.loads() 的参数是字典.
# json.dump() 和 json.load() 的参数是文件.
with open('dump.json','wb') as f:
	json.dump({'a':1,'b':2,'c':3},f)


# 如何解析简单的XML文档
from xml.etree.ElementTree import parse
f = open('demo.xml')
et = parse(f)
root = et.getroot()  #获取根节点
root.tag  #获取元素标签
for child in root:
	print(child.get('name'))


# 如何读写excel文件?
import xlrd,xlwt
book = xlrd.open_workbook('demo.xlsx')
sheet = book.sheet_by_index(0)  #根据索引获取excel文件的sheet
sheet = book.sheet_by_name('sheetname')  #根据sheet名获取Excel文件的sheet
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell(0,0))
print(sheet.row(1))

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
wsheet.write(row,col,label)
wbook.save('output.xlsx')
================================================
import xlrd,xlwt
rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,'总分',None)
for row in range(1,rsheet.nrows):
	total = sum(rsheet.row_values(row,1))
	rsheet.put_cell(row,nc,xlrd.XL_CELL_TEXT,total,None)
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align:vertical center,horizontal center')
for r in range(rsheet.nrows):
	for c in range(rsheet.ncols):
		wsheet.write(r,c,rsheet.cell_values(r,c),style)
wbook.save('output.xlsx')
================================================


# 如何派生内置不可变类型并修改其实例化行为?
# 实际案例:想自定义一种新类型的元组,对于传入的可迭代对象,只保留其中int类型且值大于0的元素,例如:IntTuple([1,-1,'abc',6,['x','y'],3]) ==> (1,6,3) 要求IntTuple是内置tuple的子类,如何实现?
class IntTuple(tuple):
	def __new__(cls,iterable):
		g = (x for x in iterable if isinstance(x,int) and x > 0)
        return super(IntTuple,cls).__new__(cls,g)
	def __init__(self,iterable):
		super(IntTuple,self).__init__(iterable)


# 如何为创建大量实例节省内存?
# 解决方案:定义类的__slots__属性,它是用来声明实例属性名字的列表.
import sys
sys.getsizeof(object, default)  #查看对象的消耗内存大小
class Player(object):
	__slots__ = ['id','name','age','job']	#绑定实例化属性,属性实例化之后无法拓展,达到节省内存消耗的目的
	def __init__(self,id,name,age,job):
		self.id = id
		self.name = name
		self.age = age
		self.job = job

# 如何让对象支持上下文管理?
# 实际案例:我们实现了一个telnet客户端的类TelnetClient,调用实例的start()方法启动客户端与服务器交互,交互完毕后需调用cleanup()方法,关闭已连接的socket,以及将操作历史记录写入文件并关闭.    能否让TelnetClient的实例支持上下文管理协议,从而替代手工调用cleanup()方法???
解决方案:实现上下文管理协议,需定义实例的__enter__,__exit__方法,它们分别在with开始和结束时被调用

from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque
class TelnetClient(object):
	def __init__(self,addr,port=23):
		self.addr = addr
		self.port = port
		self.tn = None
	def start(self):
		self.tn = Telnet(self.addr,self.port)
		self.history = deque()
		# user
		t = self.tn.read_until('login:')
		stdout.write(t)
		user = stdin.readline()
		self.tn.write(user)
		# password
		t = self.tn.read_until('Password:')
		if t.startswith(user[:-1]):t = t[len(user) + 1:]
		stdout.write(t)
		self.tn.write(stdin.readline())

		t = self.tn.read_until('$ ')
		stdout.write(t)
		while True:
			uinput = stdin.readline()
			if not uinput:
				break
			self.history.append(uinput)
			self.tn.write(uinput)
			t = self.tn.read_until('$ ')
			stdout.write(t[len(uinput) + 1:])

	# def cleanup(self):
	# 	self.tn.close()
	# 	self.tn = None
	# 	with open(self.addr + '_history.txt','w') as f:
	# 		f.writelines(self.history)

 	def __enter__(self):
 		self.tn = Telnet(self.addr,self.port)
 		self.history = deque()
 		return self
 	def __exit__(self,exc_type,exc_val,exc_tb):
 		self.tn.close()
 		self.tn = None
 		with open(self.addr + '_history.txt','w') as f:
 			f.writelines(self.history)

 with TelnetClient('127.0.0.1') as client:
 	client.start()


 # 如何创建可管理的对象属性?
 # 使用调用方法在形式上不如访问属性简洁,能否在形式上是属性访问,实际上是调用方法?
 # 解决方案:使用property函数为类创建可管理属性,fget/fset/fdel对应相应属性
 from math import pi
 class Circle(object):
 	def __init__(self,radius):
 		self.radius = radius
 	def getRadius(self):
 		return self.radius
 	def setRadius(self,value):
 		if not isinstance(value, (int, long, float)):
 			raise ValueError('wrong type.')
 		self.radius = float(value)
 	def getArea(self):
 		return self.radius ** 2 * pi
 	R = property(getRadius, setRadius)


 # 如何让类支持比较操作
 # 解决方案:比较符号运算重载,需要实现以下方法:__lt__,__le__,__gt__,__ge__,__eq__,__ne__ .
class Rectangle(object):
	def __init__(self,w,h):
		self.h = h
		self.w = w
	def area(self):
		return self.w * self.h

	def __lt__(self,obj):
		return self.area() < obj.area()
	def __le__(self,obj):
		return self.area() <= obj.area()
	def __gt__(self,obj):
		return self.area() > obj.area()
	def __ge__(self,obj):
		return self.area() >= obj.area()
	def __eq__(self,obj):
		return self.area() == obj.area()
	def __ne__(self,obj):
		return self.area() != obj.area()
# 使用标准库下的functools下的类装饰器可以简化此过程
from functools import total_ordering
@total_ordering
class Rectangle(object):
	def __init__(self,w,h):
		self.h = h
		self.w = w
	def area(self):
		return self.w * self.h
	def __eq__(self,obj):
		return self.area() == obj.area()
	def __lt__(self,obj):
		return self.area() < obj.area()

 # 如何使用描述符对实例属性做类型检查?
 # 实际案例:在某项目中,实现了一些类,希望能像静态类型语言那样对实例属性做类型检查
 # 要求:1 可以对实例变量名指定类型 2 赋予不正确的类型时抛出异常
 # 解决方案:使用描述符来实现需要类型检查的属性:分别实现__get__,__set__,__delete__ 方法,在__set__内使用isinstance函数做类型检查
 class  Attr(object):
 	"""docstring for  Attr"""
 	def __init__(self, name,type_):
 		'''定义属性和对应的类型'''
 		self.name = name
 		self.type = type_
 	def __get__(self,instance,cls):
 		return instance.__dict__[self.name]
 	def __set__(self,instance,value):
 		if not isinstance(value,self.type_):
 			raise TypeError('expected an %s' % self.type_)
 		instance.__dict__[self.name] = value
 	def __delete__(self,instance):
 		del instance.__dict__[self.name]

 class Person(object):
 	name = Attr('name', str)
 	age = Attr('age', int)
 	height = Attr('height', float)

 # 如何在环状数据结构中管理内存?
 # python中垃圾回收器通过引用计数来回收垃圾对象,某些环状数据结构存在对象间的循环引用,同时del掉引用的节点,两个对象不能被立即回收,该如何解决?
 # 解决方案:使用标准库weakref,可以创建一种能访问对象但不增加引用计数的对象(类似于Objective-C中的弱引用)
import sys
sys.getrefcount(object)  #查看对象的引用计数
import weakref
class Data(object):
	"""docstring for Data"""
	def __init__(self, value,owner):
		# self.owner = owner
		self.owner = weakref.ref(owner)
		self.value = value
	def __str__(self):
		return "%s's data,value is %s" % (self.owner,self.value)
	def __del__(self):
		print('in Data.__del__')
class Node(object):
	def __init__(self,value):
		self.data = Data(value, self)
	def __del__(self):
		print('in Node.__del__')

node = Node(100)
del node


# 如何通过实例方法名字的字符串调用方法
# 实际案例:项目中代码使用了三个不同库中的图形类:Circle,Triangle,Rectangle. 每个类都有一个获取图形面积的接口(方法),但接口名字不同,我们可以实现一个统一的获取面积的函数,使用每种方法名进行尝试,调用相应类的接口
# 解决方案:1 使用内置函数getattr,通过名字在实例上获取方法对象,然后调用. 2 使用标准库中的operator下的methodcaller函数调用
class Circle(object):
	pass
class Triangle(object):
	pass
class Rectangle(object):
	pass

def getArea(shape):
	for name in ('area','getarea','get_area'):
		f = getattr(shape, name, None)
		if f:
			return f()
s1 = Circle(2)
s2 = Rectangle(3,3)
s3 = Triangle(2,3,4)
shapes = [s1,s2,s3]
print(getArea,shapes)

from operator import methodcaller
s = 'abc123abc321'
s.find('abc', 3)
methodcaller('find','abc',4)


# 如何使用多线程?
====================================================
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from StringIO import StringIO
from xml_pretty import pretty
def download(url):
	response = requests.get(url,timeout=3)
	if response.ok:
		return StringIO(response.content)
def csvToXml(scsv,fxml):
	reader = csv.reader(scsv)
	headers = reader.next()
	headers = map(lambda h:h.replace(' ',''),headers)

	root = Element('Data')
	for row in reader:
		eRow = Element('Row')
		root.append(eRow)
		for tag,text in zip(headers,row):
			e = Element(tag)
			e.text = text
			eRow.append(e)
	pretty(root)
	et = ElementTree(root)
	et.write(fxml)

# if __name__ == "__main__":
# 	url = "http://table.finance.yahoo.com/table.csv?s=000001.sz"
# 	rf = download(url)
# 	if rf:
# 		with open('000001.xml','wb') as wf:
# 			csvToXml(rf,wf)
====================================================
def handle(sid):
	print('Downloading...(%d)' % sid)
	url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
	url %= str(sid).rjust(6, '0')  #股票代码000001,只需传入1即可,其它数字自动以0填充
	rf = download(url)
	if rf is None:return
	print('Covert to XML...(%d)' % sid)
	fname = str(sid).rjust(6, '0') + '.xml'
	with open(fname,'wb') as wf:
		csvToXml(rf, wf)

from threading import Thread
# 方法1:
t = Thread(target=handle,args=(1,))
t.start()
print('main thread')
# 方法2:
class MyThread(Thread):
	def __init__(self,sid):
		Thread.__init__(self)
		self.sid = sid
	def run(self):
		handle(self.sid)

threadList = []
for i in range(1,11)
	t = MyThread(i)
	threadList.append(t)
	t.start()

for t in threadList:
	t.join() #阻塞函数,会让子线程全部退出之后主线程再退出
print('main thread')



# 如何线程间通信?
====================================================
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from StringIO import StringIO
from xml_pretty import pretty
from threading import Thread
from Queue import Queue

class DownloadThread(Thread):	#下载线程类
	def __init__(self,sid):
		Thread.__init__(self)
		self.sid = sid
		self.url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
		self.url %= str(sid).rjust(6, '0')
	def download(self,url):
		response = requests.get(url,timeout=3)
		if response.ok:
			return StringIO(response.content)
	def run(self):  #线程入口方法
		print('Download',self.sid)
		data = self.download(self.url)
		self.queue.put((self.sid,data))

class ConvertThread(Thread):
	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue

	def csvToXml(self,scsv,fxml):
		reader = csv.reader(scsv)
		headers = reader.next()
		headers = map(lambda h:h.replace(' ',''),headers)

		root = Element('Data')
		for row in reader:
			eRow = Element('Row')
			root.append(eRow)
			for tag,text in zip(headers,row):
				e = Element(tag)
				e.text = text
				eRow.append(e)
		pretty(root)
		et = ElementTree(root)
		et.write(fxml)
	def run(self):
		while True:
			sid,data = self.queue.get()
			print('Convert',sid)
			if sid == -1:
				break
			if data:
				fname = str(sid).rjust(6, '0') + '.xml'
				with open(fname,'wb') as wf:
					self.csvToXml(data, wf)

q = Queue()
dThreads = [DownloadThread(i,q) for i in range(1,11)]
cThread = ConvertThread(q)
for t in dThreads:
	t.start()
cThread.start()

for t in dThreads:
	t.join()
q.put(-1,None)
====================================================

# 如何使用函数装饰器?
# 定义装饰器函数,用来生成一个在原函数基础添加了新功能的函数,替代原函数
def memo(func):
	cache = {}
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap
@memo
def fibonacci(n):
	"""斐波那契数列"""
	return 1 if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# 没有装饰器函数,需修改原函数以提高运算效率:
def fibonacci2(n,cache=None):
	if cache is None:
		cache = {}  #创建新字典
	if n in cache:
		return cache[n]  #返回n的值
	if n <= 1:
		return 1
	cache[n] = fibonacci2(n-1,cache) + fibonacci2(n-2,cache)


# 10个台阶的楼梯,从下面走到上面,一次只能迈1-3个台阶,且不能后退,走完楼梯共有多少种方法.
@memo
def climb(n,steps):
	count = 0
	if n == 0:
		count = 1
	elif n > 0:
		for step in steps:
			count += climb(n-step, steps)
	return count

如何为被装饰的函数保存元数据?
# f.__name__  函数的名字
# f.__doc__   函数的文档字符串
# f.__moudle__  函数所属模块名
# f.__dict__  默认字典
# f.__defaults__  默认参数元组
# 使用装饰器后,再使用上面这些属性访问时,看到的是内部包裹函数的元数据,原来函数的元数据便丢失掉了,应该如何解决?
====================================================
from functools import update_wrapper,wraps
def mydecrator(func):
	@wraps(func)
	def wrapper(*args,*kargs):
		'''wrapper function'''
		print('In wrapper!')
		func(*args,*kargs)
	# update_wrapper(wrapper, func,('__name__','__doc__',''),('__dict__'))
	return wrapper

@mydecrator
def example():
	'''example function'''
	print('In example')
print(example.__name__)
print(example.__doc__)
====================================================

# 如何实现属性可修改的函数装饰器?
为分析程序内哪些函数执行时间开销较大,定义一个带timeout的函数装饰器,装饰功能如下: 1 统计被装饰函数单次调用运行时间 2 时间大于参数timeout的,将此次函数调用记录到log日志中 3 运行时可修改timeout的值.

from functools import wraps
import time
import logging

def warn(timeout):
    def decorator(func):
    	def wrapper(*args,**kargs):
    		start = time.time()
    		res = func(*args,**kargs)
    		used = time.time() - start
    		if used > timeout:
    			msg = '%s:%s > %s' % (func.__name__,used,timeout)
    			logging.warn(msg)
    		return res
    	def setTimeout(k):
    		nonlocal timeout
    		timeout = k
    	wrapper.setTimeout = setTimeout
    	return wrapper
    return decorator


from random import randint
@warn(1.5)
def test():
	print("In test")
	while randint(0, 1):
		time.sleep(0.5)

for _ in range(30):
	test()
