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

