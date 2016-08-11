'''
Created on 2016年7月27日

@author: Administrator

元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
'''
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)