'''
Created on 2016年8月4日

@author: Administrator

pickling序列化, 反序列化即unpickling
'''
import pickle

d = dict(name='Bob', age=20, score=88)
# 把任意对象序列化成一个bytes
print(pickle.dumps(d))

# 序列化
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
    
# 反序列化
with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print('反序列化：', d)