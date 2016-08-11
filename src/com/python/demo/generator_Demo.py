'''
Created on 2016年7月27日

@author: Administrator

生成器：generator
创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
'''
#列表生成式
print([x * x for x in range(1, 11)])
    
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])

#生成器
g = (x * x for x in range(1, 11))
print(g)

for n in g:
    print(n)
    
print('--------------')
#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(_max):
    n, a, b = 0, 0, 1
    result = [];
    while n < _max:
        result.append(b)
        #a,b = b,a+b 相当于：
        #temp = b
        #b = a + b
        #a = temp
        a, b = b, a + b
        print('a=',a,'b=',b)
        n = n + 1
    return result

print(fib(8))

#generator函数在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fibs(num):
    a=b=1
    for _i in range(num):
        yield a
        a,b=b,a+b
        
print(list(fibs(8)))

print('--------------')
#杨辉三角
def pas_triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
 
#在if __name__ == "__main__"：之后的语句作为模块被调用的时候，语句之后的代码不执行；直接使用的时候，语句之后的代码执行
if __name__ == "__main__":
    g = pas_triangles()
    for n in range(10):
        print(next(g))
  
print('--------------')
#zip([seql, ...])接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
#若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同      
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = zip(a, b)
#print(dir(a))  # 查看a的相关属性
for i in z: print(i)

s = zip(*zip(a, b))
for i in s: print(i)

#首字母大写，其他小写
def normalize(*name): 
    L2 = [s.capitalize() for s in name ] 
    return L2 

def normalize2(name): 
    r1 = name[0].upper() 
    r2 = name[1: ].lower() 
    return ('%s%s' % (r1,r2))

L1 = ['adam', 'LISA', 'barT'] 
L2 = list(map(normalize2, L1)) 
print (L2)

#filter()函数用于过滤序列
def not_empty(s):
    return s and s.strip()

l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l)

#排序
t = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(t)
t = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(t)
