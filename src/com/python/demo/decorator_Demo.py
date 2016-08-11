'''
Created on 2016年7月27日

@author: Administrator

“装饰器”（Decorator）

'''
import functools

#首先打印日志，再紧接着调用原始函数。
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def log3(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if callable(text[0]) :
                print('call %s():' % (func.__name__))
            else:
                print('%s %s():' % (text[0], func.__name__))
            return func(*args, **kw)
        return wrapper
    if callable(text[0]) :
        return decorator(text[0])
    else:
        return decorator

@log
def now():
    print('2015-3-25')
    
@log2('execute')
def now2():
    print('2015-3-25')
    
@log3
# @log3('execute')
def now3():
    print('2015-3-25')
    
now()
print('---------------')
now2()
print('---------------')
now3()