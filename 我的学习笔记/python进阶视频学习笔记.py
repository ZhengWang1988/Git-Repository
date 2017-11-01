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
