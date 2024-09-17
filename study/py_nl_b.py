#简单回顾
# #定义类
# class Person:
#     name = 'dingding'  #类属性
#     def run(self):     #self代表对象本身,实例方法，没有这个会报错
#         print('run方法中的self:',self)
#         print('人类会跑步')
# #实例化对象：对象名 = 类名（）
# pe = Person()
# print(pe)
# pe.run()

#1.实例方法和实例属性
#实例属性
#格式：self.属性名
# class Person:
#     name = 'dingding'  #类属性
#     def introduce(self):#实例方法
#         print('我是实例方法')
#         print(f'{Person.name}的年龄：{self.age}')  #self.age时实例属性
# pe = Person()
# pe.age = 18
# pe.introduce()

#1.2实例属性和类属性的区别
#类属性属于类，是公共的，大家都能访问到，实例属性属于对象的，是私有的
#只能由对象名访问，不能类名访问
# class Person:
#     name = 'dingding'  #类属性
#     def introduce(self):#实例方法
#         print('我是实例方法')
#         print(f'{self.name}的年龄：{self.age}')  #self.age时实例属性
# pe = Person()
# pe.age = 18
# pe.sex = '女'   #实例属性
# print(pe.sex)  #根据对象名访问实例属性
# print(Person.sex)  #报错--实例属性只能由对象名访问，不能类名访问
# pe.introduce()
#访问类属性，类可以访问到，实例对象也可以访问到
# print(Person.name)
# print(pe.name)
# pe2 = Person()
# # print(pe2.sex)  #报错--pe.sex='女'是给pe对象新增的实例属性，其他对象依然是没有这个属性
# pe2.sex = '男'
# print(pe2.sex)
#每实例化一次就需要添加一次，效率不高

#构造函数  __init__()
#作用：通常用来做属性初始化或者赋值操作
#注意：在类实例化对象的时候，会被自动调用
# class Test:
#     def __init__(self):   #self--实例方法
#         print('这是__init__()函数')
#实例化对象：对象名 = 类名（）
# te = Test()
class Person:  #人类
    def __init__(self,name,age,height):
        self.name = name  #实例属性  姓名
        self.age = age
        self.height = height
    def play(self):
        print(f'{self.name}在打流浪体')
    def introduce(self):
        print(f'{self.name}的年龄是{self.age},身高是{self.height}cm')
#实例化对象
pe = Person('dingding',22,160)
pe.introduce()
pe.play()
#实例化第二个对象
pe2 = Person('qiaoqiao',28,187)
pe2.play()
pe2.introduce()
#实例化第三个对象
pe3 = Person('yangyang',15,175)
pe3.play()
pe3.introduce()