'''
Created on 2016年8月4日

@author: Administrator
'''
from datetime import datetime

try:
    f = open('D:\pythonWorkspace\pthonDemo\src\com\python\demo\Exception.txt', 'r')
#     print(f.read())会一次性读取文件的全部内容
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
finally:
    if f:
        f.close()
        
print('--------------')
# with语句自动帮我们调用close()方法
# errors='ignore'遇到编码错误后直接忽略
with open('D:\pythonWorkspace\pthonDemo\src\com\python\demo\Exception.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())
 
print('--------------读取二进制文件')   
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
with open('D:\pythonWorkspace\pthonDemo\src\com\python\demo\Exception.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
    
print('--------------写文件')
with open('test.txt', 'w', encoding='UTF-8') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))