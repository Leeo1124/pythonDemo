'''
Created on 2016年7月27日

@author: Administrator
'''
import logging
# 有debug，info，warning，error等几个级别
logging.basicConfig(level=logging.INFO)

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
    logging.exception(e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    logging.exception(e)#记录错误信息
else:
    print('no error!')
finally:
    print('finally...')
print('END')


#自定义错误类型
class FooError(ValueError):
    pass

# 用raise语句抛出一个错误的实例
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo('0')

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise#raise语句如果不带参数，就会把当前错误原样抛出

bar()