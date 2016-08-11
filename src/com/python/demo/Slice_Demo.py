'''
Created on 2016年7月27日

@author: Administrator

切片（Slice）操作符
'''

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前3个元素
print(L[0:3])
print(L[:3])

#取倒数第一个元素
print(L[-1:])

print(L[-2:-1])

L = list(range(100))
print(L)

#前10个数，每两个取一个
print(L[:10:2])

#所有数，每5个取一个
print(L[::5])

#可以原样复制一个list
print(L[:])

print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])