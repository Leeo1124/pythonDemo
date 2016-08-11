'''
Created on 2016年7月27日

@author: Administrator

'''
import math

#通过help(abs)查看abs函数的帮助信息
help(abs)

#求绝对值
print(abs(-200))

#max()可以接收任意多个参数，并返回最大的那个
print(max(2, 3, 1, -5))

#数据类型转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数

#定义函数
#数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
print(my_abs(-200))

#空函数
def nop():
    pass

#返回多个值的函数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#函数可以同时返回多个值，但其实就是一个tuple
r = move(100, 100, 60, math.pi / 6)
print(r)

#默认参数,必选参数在前，默认参数在后，否则Python的解释器会报错;默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))

#可变参数
def calc(*numbers):
    _sum = 0
    for n in numbers:
        _sum = _sum + n * n
    return _sum

print(calc(1, 2))
print(calc())
nums = [1, 2, 3]
print(*nums)

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数
#限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)
    
person2('Jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
    
person3('Jack', 24, city='Beijing', job='Engineer')
    
#命名关键字参数可以有缺省值
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
    
person4('Jack', 24, job='Engineer')

#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)