# 1.函数
# 1.1含义：将独立的代码块组织成一个整体，事情具有特殊功能的代码集合，在需要的时候调用即可
# 1.2作用：提高代码的重用性，使整体代码看上去更加简练
# 1.3 基本格式
# 1.3.1定义函数
# def 函数名():
#   函数体
# 1.3.2调用函数
# 函数名()
def login():
    print('这是登录函数')
login()
login()
#调用几次，函数里面的代码就会运行几次，每次运行的时候，函数都会从头开始运行

#编写一个打招呼的函数并调用
#say_hello()   #报错--调用函数前必须先定义
def say_hello():
    print('hello')
    print('dingding')
    print('22岁')
say_hello()



# 2.返回值 return
# 函数执行结束后，最后给调用者的一个结果。
#作用：
#   1.return会给函数的执行者返回值
#     def buy1():
#         return '一瓶哇哈哈'
#     buy1()
#     print(buy1())
#   2.函数中遇到return,表示此函数结束，不继续执行
#     def buy2():
#         return '一瓶哇哈哈',20   #('一瓶哇哈哈',20)--return返回多个值以元组的形式返回给调用值
#         #return '20'  #函数中遇到return,下面的代码不执行
#     print(buy2())

#返回值的三种情况：
#   1.一个返回值也没有，返回的结果是None
#   2.一个返回值，就把值返给调用者
#   3.多个返回值，以元组的形式返回调用

#return和print的区别
#   1.return表示此函数结束，print会一直执行
#     def funa():
#         #return 123
#         print(456)
#     print(funa())
#   2.return是返回计算值，print是打印结果
#     def funb():
#         a = 1
#         b = 2
#         return a + b  #print(a + b)
#     print(funb())     #funb()



# 3.参数
#定义格式：
# def 函数名(形参a,形参b)  #形参是定义函数时，小括号里的变量
#     函数体
#     ...(如a=1,b=2)
# 调用格式:
# 函数名(实参1,实参2)      #实参是调用函数是，小括号里具体的值
def add(a,b):
    return a+b
print(add(1,2))

#3.1 函数参数
#3.1.1 必备参数（位置参数）
#含义：传递和定义参数的顺序及个数必须一致
#格式：def func(a,b):
def func(name,name2,name3):
    print(name)
    print(name2)
    print(name3)
func('dingding','qiaoqiao','rourou') #写了几个就必须要传几个，不可以多传少传

#3.1.2 默认参数
#含义：为参数提供默认值，调用参数时可不传该默认参数的值
#注意：所有的位置参数必须出现在默认参数前，包括函数定义和调用
#格式：def func(a=12)
def fund(b,a=8):
    print(b)
fund()  #8
fund(200)#200
#设置默认值，没有传值会根据默认值来执行代码，传了值根据传入的值来执行代码

#3.1.3可变参数
#含义：传入的值的数量是可以改变的，可以传入多个，也可以不传
#格式：def func(*args)
def fune(*args):  #可以把args改成其他参数名。但args更规范
    print(args)
    print(type(args))  #以元组形式接收
fune('胡图图','牛爷爷')

#3.1.4关键字参数
#格式：def func(**kargs)
def funf(**kargs):  #可以把kargs改成其他参数名。但args更规范
    print(kargs)
    print(type(kargs))  #以字典形式接收
funf()  #空字典
fune(name='dingding',age=18)    #传值的时候，需要采用键值对的形式
#作用：可以扩展函数的功能


#4.函数嵌套
#4.1嵌套调用
#含义：在一个函数里面调用另外一个函数
def study1():
    print('晚上在学习')
def course1():
    study1()  #在course里调用study
    print('Python基础')
#4.2嵌套定义
#含义：在一个函数中定义另外一个函数
def study2():  #外函数
    print('晚上在学习')
    def course2():  #内函数
        print('Python基础')  #不要在内层函数中调用外层函数
    course2()  #定义和调用是同级的注意缩进
study2()
