'''
Created on 2016年8月4日

@author: Administrator
'''
import os
import shutil
from datetime import datetime

# #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# print(os.name) # 操作系统类型
# # print(os.uname())uname()函数在Windows上不提供
#  
# #环境变量
# print(os.environ)
# print(os.environ.get('PATH'))
#  
# # 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
#  
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('D:/Users/michael', 'testdir'))
#  
# # 然后创建一个目录:
# os.mkdir('D:/testdir')
# # 删掉一个目录:
# os.rmdir('D:/testdir')
#  
# # 拆分路径
# print(os.path.split('/Users/michael/testdir/file.txt'))
# # 得到文件扩展名
# print(os.path.splitext('/path/to/file.txt'))
#  
# # 对文件重命名:
# os.rename('test.txt', 'test.py')
# # 删掉文件:
# os.remove('test.py')

#过滤文件
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)

# 复制文件
shutil.copyfile('test.txt', 'test2.txt')



pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M:%S')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))