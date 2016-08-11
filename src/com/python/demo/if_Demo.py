'''
Created on 2016年7月27日

@author: Administrator
'''
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
    
    
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = -1
if x:
    print('True')