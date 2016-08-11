'''
Created on 2016年8月10日

@author: Administrator
'''
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

# 字符+和/，在URL中就不能直接作为参数,urlsafe_b64encode把字符+和/分别变成-和_
s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)