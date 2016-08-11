'''
Created on 2016年8月11日

@author: Administrator

协程
'''
def consumer():
    r = ''
    while True:
        #因为此处为无限循环，所以从send(None)开始，每次yield返回值后都会停留在此。
        #这里的(yield r)为一个表达式，值为send(msg)传递的msg，返回的为r的值，第一次send(None)时，yield直接返回r值后，便停止在这里：
        n = yield r
        print('----:',n)
        if not n:
            print('被执行过！')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK' + r

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        #此处c.send(n)在传递完n的值后，每次都返回(yield r)的值，也就是r的值
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)