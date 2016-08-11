'''
Created on 2016年8月3日

@author: Administrator
'''
from types import MethodType

class Student(object):
    '''
    classdocs
    '''

    def __init__(self, name, score):
        '''
        Constructor
        '''
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score
     
    #把一个getter方法变成属性   
    @property
    def score(self):
        return self._score

    #把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
bart = Student('Bart Simpson', 98)
bart.print_score()
# print(bart.__name)私有方法，外部不能访问
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(bart._Student__name)
bart.set_name('aaa')
bart.print_score()

#给实例绑定一个方法,给一个实例绑定的方法，对另一个实例是不起作用
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
    
bart.set_age = MethodType(set_age, bart) # 给实例绑定一个方法
bart.set_age(25)# 调用实例方法
print(bart.age)

s2 = Student('hcy', 100)
# print(s2.age)

#给class绑定方法后，所有实例均可调用
Student.set_age = set_age
s2.set_age(100)
print(s2.age)

print('-----------')
s2.score = 60
print(s2.score)