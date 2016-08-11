#输出
print('hello python!')
print(100 + 200 + 300)
print('100 + 200 =', 100 + 200)
print("adfa")
print('The quick brown fox', 'jumps over', 'the lazy dog')

#输入
#name = input('please enter your name: ')
#print('hello',name)

#用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

#用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

print(r'''\\\t\\line1
line2
line3''')

print(True and True)
print(True or True)
print(not True)

print(10 / 3)
print(10 // 3)

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

#bytes类型的数据用带b前缀的单引号或双引号表示
print('ABC'.encode('ascii'))
print(b'ABC'.decode('ascii'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('中文'))
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

print('Hi, %s, you have $%d.' % ('Michael', 1000000))