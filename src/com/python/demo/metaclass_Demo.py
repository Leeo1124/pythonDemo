'''
Created on 2016年7月27日

@author: Administrator
'''
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 要创建一个class对象，type()函数依次传入3个参数：
# 
#     1、class的名称；
#     2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#     3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
    
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
print(type(Hello))
print(type(h))


# metaclass是类的模板，所以必须从`type`类型派生：
# metaclass可以给我们自定义的MyList增加一个add方法
# __new__()方法接收到的参数依次是：
# 
#     1、当前准备创建的类的对象；
# 
#     2、类的名字；
# 
#     3、类继承的父类集合；
# 
#     4、类的方法集合。

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
class MyList(list, metaclass=ListMetaclass):
    pass

print('--------------')
L = MyList()
L.add(1)
print(L)

# 普通的list没有add()方法
L2 = list()
L2.add(1)
print(L2)