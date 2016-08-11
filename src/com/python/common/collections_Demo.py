'''
Created on 2016年8月10日

@author: Administrator
'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

from collections import deque

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict

# 如果希望key不存在时，返回一个默认值
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

from collections import OrderedDict

# dict的Key是无序的
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# OrderedDict的Key是有序的,Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

from collections import Counter

# 统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)