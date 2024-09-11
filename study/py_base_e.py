#1.装饰器
# def test02():
#     print('发送消息给丁丁')
# def test():
#     print('开始注册')
#     print('登录')
#     fn()  #调用要传入的函数
# test(test02())
#含义：装饰器本质上就是一个闭包函数，在不改变原有代码情况下添加新的功能
#条件：
#   1.不修改源程序或函数的代码
#   2.不改变函数或程序的调用方法

#1.1闭包的三个条件
#   1.函数嵌套（函数里面再定义函数）
#   2.内层函数使用外层函数的局部变量
#   3.外层函数的返回值是内层函数的函数名

#1.2 标准版装饰器
# def send():
#     print('发送消息')
# #send()
# def send2():
#     print('转账520')
# #装饰器函数
# def outer(fn): #外层函数，fn是形参，但是往里面传入的是被装饰的函数名：send
#     #既包含原有功能，又包含新功能
#     def inner():  #内函数
#         print('登录')
#         #执行被装饰的函数
#         fn()   #send()
#     return inner
# print(outer(send))
# ot = outer(send2)  #调用外函数
# ot()               #调用内函数

#装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包

#1.3 语法糖
#格式：@装饰器名称
# def outer(fn):
#     def inner():
#         print('登录')
#         #执行被装饰的函数
#         fn()
#     return inner
# #注意装饰器后面不要加（），前者是引用，后者是调用函数，返回该函数要返回的值。最好顶格写，也不要空行
# @outer  #不可以加括号写成-@outer()
# def send():
#     print('发送消息:hhh')
# send()
# def send2():
#     print('发送消息：qqq')
# send2()

#1.4被装饰的函数有参数
# def outer(fn):
#     def inner(name): #内函数，name是内函数的参数
#         print(f'{name}是inner函数中的参数')
#         print('hh')
#         fn(name)
#     return inner
# @outer
# def func(name):  #不写name要报错
#     print('这是被装饰的函数')
# func('dingding') #不写dingding也要报错
# #此语法糖的标准装饰器形式
# ot = outer(func)  #ot = inner
# ot('dingding')    #不写dingding要报错，调用内函数

#1.5被装饰的函数有可变参数
#被装饰的函数
# def func(*args, **kwargs):
#     print(args)  #这里不用加*
#     print(kwargs)
# func(name='dingding',age='22')
# #装饰器函数
# def outer(fn):
#     def inner():
#         print('登录')
#         fn()
#     return inner
# #函数必须被调用才会执行
# # print(outer('hello')) #outer('hello')此时相当于inner
# # outer('hello')()
# print(outer(func))
# outer(func)()

#1.6多个装饰器
#第一个装饰器
def deco1(fn):
    def inner():
        return 'hello '+fn()+' dingding'
    return inner
#第二个装饰器
def deco2(fn):
    def inner():
        return 'hi '+fn()+' qiaoqiao'
    return inner
#被装饰的函数
@deco1   # 仅装饰这一个时--hello +test1()+ dingding
@deco2   #装饰两个时--hello+ hi smart qiaoqiao +dingding
def test1():
    return 'smart'
print(test1()) #hello +test1()+ dingding
#多个装饰器的装饰过程，离函数最近的装饰器现状是，然后外面的装饰器再进行装饰，由内到外的装饰过程


