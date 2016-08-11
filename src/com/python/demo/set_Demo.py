'''
Created on 2016年7月27日

@author: Administrator

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key

'''

s = set([1, 1, 2, 2, 3, 3])
print(s)

#添加元素
s.add(4)
print(s)

#删除元素
s.remove(4)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)