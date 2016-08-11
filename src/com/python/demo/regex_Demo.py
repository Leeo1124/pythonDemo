'''
Created on 2016年8月9日

@author: Administrator
'''
import re

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

t = '19:05:30'
print('Test:', t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 正则匹配默认是贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 预编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())