# 1.作用域
# 1.1含义：指的是变量生效的范围，分为两种，分别是全局变量和局部变量
# 1.2全局变量
# 函数外部定义的变量，在整个文件中都是有效的
from study.py_base_a import name1

a = 100 #全局变量
def test1():
    print('这是test1中a的值',a)
def test2():
    a = 120 #局部变量
    print('这是test2中a的值',a)
print('调用函数前a的值',a)
test1()
test2()
print('调用函数后a的值',a)
# a的值没有被覆盖是因为函数内部如果要使用变量，环线从函数内部找，有的话就直接使用，没有会到函数外面去找

#1.3局部变量
#函数内部定义的变量，从定义位置开始到函数定义结束位置有效
def funa():
    num = 10  #局部变量
    print('num',num)
funa()
# print('num',num)  #报错--局部变量只能在被定义的函数中使用，函数外部不能使用
#作用：在函数体内部，临时保存数据，当函数调用完成后就销毁局部变量
def funb():
    num = 10  #局部变量
    print('funb中的num',num)
funb()
def func():
    num = 18  #局部变量
    print('func中的num',num)
func()

#全局变量和局部变量命名相同
#在函数内部修改全局变量的值，可以使用global关键字
#global
#将变量声明为全局变量
#语法格式：global 变量名
a = 100 #全局变量
def test3():
    print('这是test3中a的值',a)
def test4():
    global a  #声明全局变量--不可以global a = 120注意格式
    a = 120 #局部变量
    print('这是test4中a的值',a)
print('调用函数前a的值',a)
test3()
test4()
print('调用函数后a的值',a)

def study():
    global name
    name = 'py基础'
    print(f'我们在学习{name}')
study()
print(name)
def work():
    print(name)
work()

#总结：global关键字剋有对全局变量中进行修改，也可以在局部作用域中声明一个全局变量

#1.5 nonlocal--了解
#用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明
a = 10  #全局变量
def outer():
    a = 5
    def inner():
        # nonlocal a
        a = 20
        def inner2():
            # nonlocal a
            a = 30
            print('inner2函数中a的值', a)
        inner2()
        print('inner函数中a的值',a)
    inner()
    print('outer函数中a的值',a)
outer()
#nonlocal只能对上一级进行修改


#2.匿名函数
#2.1基本语法
#函数名 = lambda 形参:返回值（表达式）
#调用：结果 = 函数名

#普通函数
def add(a,b):
    return a+b
print(add(10,20))
#匿名函数
add = lambda a,b:a+b  #a,b就是匿名函数的形参，a+b就是返回值的表达形式
#lambda不需要写return来返回值，表达式本省结果就是返回
print(add(10,20))

#2.2lambda的参数形式
#函数名 = lambda 形参:返回值（表达式）
# 2.2.1无参数
# funa = lambda :'一瓶哇哈哈'
# print(funa())
# 2.2.2一个参数
# funb = lambda x:x
# print(funb('dingding'))
# 2.2.3默认参数
# func = lambda name,age=18:(name,age)
# print(func('dingding'))
# print(func('dingding',20))
fune = lambda a,b,c=12:a+b+c
print(fune(10,20,4))
print(fune(10,20))
#默认参数必须卸载非默认参数后面
#2.2.4 关键字参数
fund = lambda **kwargs:kwargs
print(fund(name='dingding',age='18'))

#2.3lambda结合if判断
a = 8
b = 5
#为真结果if条件else为假结果
print('a比b小') if a < b else print('a大于等于b')
comp = lambda a,b:'a比b小' if a < b else 'a大于等于b'  #ab为形参，比较大小
print(comp(a,b))
#特点：
#lambda只能实现简单的逻辑，如果逻辑复杂且大妈量较大，不建议使用


#3.内置函数
#查看所有的内置函数
import builtins
print(dir(builtins))
#大写字母开头一般是内置常量名，小写字母开头一般是内置函数名

#3.2内置函数一
#3.2.1 abs():返回绝对值
#print(abs(10))
#print(abs(-10))
# 3.2.2 sum():求和
# print(sum(123))   #报错，整型不是可迭代对象，sum函数内要放可迭代对象
# print(sum(1,2,3.5))   #运算时，只要有一个为浮点数，那么结果必定是浮点数

#3.3内置函数二
#3.3.1 min():求最小值
#3.3.2 max():求最大值
print(min(+8,5,key=abs))  #传入了绝对值函数，则参数就会先求绝对值
#3.3.3 zip():将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
li = [1,2,3]
li2 = ['a','b',]
print(zip(li,li2))
#第一种方式：通过for循环
for i in zip(li,li2):
    print(i)
    print(type(i))
#如果元素个数不一致，就按照长度最短的返回
#第二种方式：换成列表打印
print(list(zip(li,li2))) #换成列表打印
#注意必须是可迭代对象
#print(list(zip(li,3)))
#3.3.4 map():可以对可迭代对象中的每一个元素进行映射，分别去执行
# map(func,iterl):func--自己定义的函数，iterl--放进去的可迭代对象
#简单来说就是对象中的每一个元素都会去执行这个函数
li = [1,2,3]
def funa(x):
    return x * 5
mp = map(funa,li)  #注意：只要写函数名，不需要加上小括号
print(mp)
#第一种方式：通过for循环
for i in mp:
    print(i)
    print(type(i))
#第二种方式：换成列表打印
print(list(mp)) #换成列表打印
#3.3.5 reduce():先把对象中的两个元素取出来，计算出其中一个值然后保存着，接下来1把这个计算值跟迪桑元素进行计算
#需要先导包
from functools import reduce
#reduce(function,sequence)  #function--函数：必须是有两个参数的函数 sequence--序列：可迭代的对象
def add(x,y):
    return x + 2*y  #1+2*2=5--5+2*3=11--11+2*4=19
res = reduce(add,[1,2,3,4])
print(res)  #19


#4.拆包
#含义：对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
tua = (1,2,3,4)
print(tua)
print(tua[0])
#方法一
#a,b,c,d=tua
#print('a=',a,'b=',b,'c=',c,'d=',d)
#要求元组内的个数与接收的变量个数相同，对象内有多少个数据就需要定义多少个变量接受
# a,b = tua #报错--值错误，要拆包的值过多
# print(a,b)
#一般在获取元组值的时候使用
#方法二
a,*b=tua
print(a,b)
c,*d=b
print(c,d)
#一般在函数调用时使用
#先把单独的取完，其他剩下的全部都交给带*的变量
def funa(a,b,*args):
    print(a,b)
    print(args,type(args))
funa(1,2,3,4,5,6,7)
arg = (1,2,3,4,5,6,7)



