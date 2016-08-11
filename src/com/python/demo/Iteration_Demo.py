'''
Created on 2016年7月27日

@author: Administrator

迭代（Iteration）
'''
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
    
for k, v in d.items():
    print(k,'=',v)
    
for ch in 'ABC':
    print(ch)
    
print(isinstance('abc', Iterable)) # str是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)
    
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)
    