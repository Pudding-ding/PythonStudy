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
# class Person:  #人类
#     def __init__(self,name,age,height):
#         self.name = name  #实例属性  姓名
#         self.age = age
#         self.height = height
#     def play(self):
#         print(f'{self.name}在打流浪体')
#     def introduce(self):
#         print(f'{self.name}的年龄是{self.age},身高是{self.height}cm')
# #实例化对象
# pe = Person('dingding',22,160)
# pe.introduce()
# pe.play()
# #实例化第二个对象
# pe2 = Person('qiaoqiao',28,187)
# pe2.play()
# pe2.introduce()
# #实例化第三个对象
# pe3 = Person('yangyang',15,175)
# pe3.play()
# pe3.introduce()


#3.析构函数__del__()
#删除对象的时候，解释器会默认调用__del__()方法
# class Person:
#     def __init__(self):
#         print('我是__init__()')
#     def __del__(self):
#         print('被销毁了')
# p = Person()
# del p  #删除p这个对象
# #del p 语句执行的时候，内存会立即被回收，会调用对象本身的__del()__
# print('这是最后第二行代码')
# print('这是最后一行代码')
#正常运行时，不会调用__del__（），对象执行结束之后，系统会自动调用__del()__
#__del__()主要是表示该程序块或者函数已经全部执行结束


#4.封装
#面向对象的三大特性：封装、继承、多态
#4.1封装：将复杂的信息、流程给包起来，内部处理，让使用者只需要通过简单的操作步骤，就能实现
      #指的是隐藏对象中一些不希望被外部所访问到的属性或者方法
# class Person:
#     name = 'dingding'  #类属性
# pe = Person()
# print(pe.name)
# Person.name = 'qiaoqiao'
# print(Person.name)

#4.2隐藏属性（私有权限），只允许在类的内部使用，无法通过对象访问
#在属性名或者方法名前面加上两个下划线__
# class Person:
#     name = 'dingding'  #类属性
#     __age = 22         #隐藏属性
#     def introduce(self):  #实例方法
#         print(f'{Person.name}的年龄是{Person.__age}')  #在实例方法中访问类属性和隐藏属性
# pe = Person()
# print(pe.name)
# # print(pe.__age)   #报错
# #第一种：了解
# #隐藏属性实际上是将名字修改为_类名__属性名  _Person__age
# # print(pe._Person__age)
# # pe._Person__age = 18
# # print(pe._Person__age)
# #第二种方式:在类的内部访问 --推荐使用，正规手段
# pe.introduce()

#私有属性/方法
#1.xxx：普通属性/方法，如果是类中定义的，则类可以在任意地方使用
#2._xxx：单下划线开头，声明私有属性/方法，如果定义在类中，外部可以使用，子类也可以继承
#        但是在另一个py文件中通过from xxx import * 导入时，无法导入
#        一般是为了避免与Python关键字冲突而采用的命名方法
#3.__xxx：双下划线开头，隐藏属性，如果定义在类中，无法在外部直接访问，子类不会继承
#         要访问只能通过间接的方式，另一个py文件中通过from xxx import *导入的时候也无法导入
#         这种命名一般是python中的魔术方法或属性，都是有特殊含义或者功能的，自己不要轻易定义
# class Person:
#     name = 'dingding'
#     __age = 28      #隐藏属性（双下划线）
#     _sex = '不男不女'#私有属性（单下划线）
# pe = Person()
# # print(pe.sex)  #报错--使用对象名._属性名调用
# print(pe._sex)
# #使用对象._类名__属性名访问隐藏属性
# print(pe._Person__age)

#4.4 隐藏方法
# class Man:
#     def __play(self):  #隐藏方法
#         print('玩手机')
#     def funa(self):   #平平无奇的实例方法
#         print('平平无奇的实例方法')
#         Man.__play(self)  #在实例方法中调用私有方法-- 不推荐
#         self.__play()     #推荐使用，更简便
# ma = Man()
# ma.funa()
# # ma._Man__play()

#4.5 私有方法
class Girl:
    def _study(self):  #私有方法
        print('整天学学学')
girl = Girl()
girl._study()



