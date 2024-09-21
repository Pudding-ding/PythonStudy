#1. __init__()和__new__()
#1.1__init__():初始化对象
# class Test(object):
#     def __init__(self):
#         print('这是__init__()')
#         print(self)
# te =Test()
#1.2__new__():object基类提供的内置静态方法
#作用：1.在内存中为对象分配空间；2.返回对象的引用
# class Test(object):
#     def __init__(self):
#         print('这是__init__()')
#         #print(self)
#     def __new__(cls, *args, **kwargs):  #后面的参数不能删掉,cls代表本身
#         print('我是__new__()')
#         print(cls)
#         #对父类方法进行扩展super().方法名（）
#         res = super().__new__(cls)
#         return res
#         # 方法重写，res里面保存的是实例对象的引用,
#         # __new__()是静态方法，形参里面有cls,实参就必须传cls
#         #注意:重写__new__()一定要return super().__new__(cls),
#         #    否则python解释器得不到分配空间的对象引用，就不会调用__init__()
# te =Test()
# print('te:',te)

#执行步骤：
#一个对象的实例化过程：首先只想__new__(),如果没有写__new__()，默认调用objest里面的__new__()，返回一个实例对象，
#                  然后再去调用__init__()，对对象进行初始化
# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print('这是new方法')
#         print('返回值：',super().__new__(cls))
#         return super().__new__(cls)
#     def __init__(self, name):
#         self.name = name  #实例属性
#         print('名字是：',self.name)
# pe = Person('dingding')
# print(pe)
# pe2 = Person('qiaoqiao')
# print(pe2)
#总结：__init__()和__new__()
#1.__new__()是创建对象，__init__()是初始化对象
#2.__new__()是返回对象引用，__init__()定义实例属性
#3.__new__()是类级别的方法，__init__()是实例级别的方法
#没有__new__()就没有__init__()



#2.单例模式
#可以理解成一个特殊的类，这个类只存在一个对象
#优点：可以节省内存空间，减少了不必要的资源浪费
#弊端:多线程访问的时候容易引发线程安全问题
#2.2 方式
    #1.通过@classmethod
    #2.通过装饰器实现
    #3.通过重写__new__()实现（重点）
    #4.通过导入模块实现

# class A(object):
#     pass
# a1 = A
# print(a1)
# a2 = A
# print(a2)
#内存地址发生变化说明是不同的对象
#实现单例模式对象的内存地址都是一样的，只有一个对象
#2.3 通过重写__new__()实现单例模式
#设计流程
#1.定义一个类属性，初始值为None,用来记录单例对象的引用
#2.重写__new__()方法
#3。进行判断，如果类属性是None，把__new__()返回的对象引用保存进去
#4.返回类属性中记录的对象引用
# class Singleton(object):
#     #记录第一个被创建对象的引用
#     obj = None #类属性
#     def __new__(cls, *args, **kwargs):
#         print('这是__new__()方法')
#         #判断类属性是否为空  （是的地址一样）
#         if cls.obj == None:
#             cls.obj = object.__new__(cls)
#         return cls.obj
#     def __init__(self):
#         print('我是__init__()')
# s = Singleton()
# print('s:',s)
# s2 = Singleton()
# print('s2:',s2)
#单例模式:每一次实例化所创建的对象都是同一个，内存地址都一样

#2.4 通过导入模块实现单例模式
#模块就是天然的单例模式
# from py_test_b import te as te01
# from py_test_b import te as te02
# print(te01,id(te01))
# print(te02,id(te02))

#2.5应用场景
#1.回收站对象
#2.音乐播放器，一个音乐播放如啊年负责音乐播放的对象只有一个
#3.开发游戏软件   场景管理器
#4.数据库配置，数据池的设计


#3.魔法方法&魔法属性
# 3.1 _doc_():类的描述信息
# class Person(object):
#     """"人类——类的描述信息"""  #只能使用多行注释，单行注释无效
#     pass
# print(Person.__doc__)

# def sing():
#     """唱歌"""
#     pass
# print(sing.__doc__)

# 3.2__module__():表示当前操作对象所在模块
# 3.3.__class__():表示当前操作对象所在的类
# import py_test_c
# b = py_test_c.B()
# print(b)
# b.funa()
# print(b.__module__)  #输出模块
# print(b.__class__)   #输出类

# 3.4__str__(): 对象的描述信息
#如果类中定义了此方法，那么在打印对象时，默认输出该方法的返回值，也就是打印方法中的return的数据
#注意：__str__()必须返回一个字符串
# class C:
#     def __str__(self):
#         return '这是str的返回值'
#         #pass   #报错--必须要有返回值，并且一定是字符串类型
# c = C()
# print(c)

# 3.5.__del__():删除对象(析构函数),在程序结束时会调用，或者在删除某个对象的时候也会被调用
# 3.6.__call__():使一个实例对象成为一个可调用对象
#可调用对象：函数、内置函数、和类都是可调用对象，凡是把一对()应用到某个对象身上都可以称为可调用对象
#callable():判断是否是可调用对象
# def func():
#     print("hhh")
# func()
# print(callable(func))  #Ture
# name = 'dingding'
# #name()
# print(callable(name))  #False

class A:
    def __call__(self, *args, **kwargs):
        print('这是__call__()')
a = A()
a()   #调用一个可调用的实例对象，其实就是在调用它的__call__()方法
print(callable(a))
# 3.7__dict__:返回对象具有的属性和方法
