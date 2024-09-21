#1.文件
#文件就是存储在某种长期储存设备上的一段数据。
#长期存储设备包括：硬盘、U盘、移动硬盘、光盘...
#1.2 文件操作
#打开文件-->读、写文件-->关闭文件
#1.3 文件对象的方法
#1.open():创建一个file对象，默认是以只读模式打开
#2.read(n):n表示从文件中读取的数据的长度，没有传n值就默认一次性读取文件的所有内容
#3.write():将指定内容写入文件
#4.close():关闭文件
#1.4 属性
#文件名.name:返回要打开的文件的文件名，可以包含文件的具体路径
#文件名.mode:返回文件的访向模式
#文件名.closed:检测文件是否关闭，关用就返回True
#1.4.1.打开文件
# f = open('test.txt')
# print(f.name)  #文件名
# print(f.mode)  #文件访问模式
# print(f.closed)
#1.4.2.关闭文件
# f.close()
# print(f.closed)

#2.文件读写操作
#2.1 read(n):n表示从文件中读取的数据的长度，没有传n值或者传的是负值默认一次性读取文件的所有内容
# f = open('test.txt')  #括号内也可以是文件存放地址
# # print(f)
# # print(f.read(-1))
# print(f.read(5))  #最多读取五个数据
# print(f.name)   #文件所在的具体路径（绝对路径）
# f.close()

#2.2 readline():一次读取一行内容，方法执行完，会把文件指针移到下一行，准备再次读取
# f = open('test.txt')
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# while True:
#     line = f.readline()  #读取一行内容
#     #读取不到内容要退出循环
#     if not line:
#         break
#     print(line)

# for i in f:
#     print(i)
#     line = f.readline()  #读取一行内容
#         #读取不到内容要退出循环
#     if not line:
#         break
# f.close()

#2.3 readlines()作用: 按照行的方式把文件内容一次性读取，返回的是一个列表，每一行的数据就是一个元素
# f = open("test.txt")
# text = f.readlines()
# print(text)
# print(type(text))
# for i in text:
#     print(i)
# f.close()

#2.4访问模式
# f = open('test.txt')
# print(f.read())#能读到文件内容
# #进行写操作
# #f.write("heiheihei") #报错--不支持写操作
# f.close()
# #因为前面讲过open()默认以只读模式打开，只能读，不能写，要写需要更改访问模式。

#2.4.1.r: 只读模式(默认模式)，文件必须存在，不存在就会报错。
#2.4.2. w: 只写模式，文件存在则会先清空文件内容，再写入添加内容，不存在则创建新文件。
# f = open('test01.txt')
# #print(f.read())     #报错，没有这个文件，找不到。
# f.close()

# f = open('test.txt','w')
# #print(f.read())     #报错，只写模式不支持读操作
# f.write("emmmm...")  #重新编辑文件内容，原先内容清空了。
# #print(f.read())     #报错
# f.close()

#2.4.3. +: 表示可以同时读写某个文件
#注意：使用+会影响文件的读写效率，开发中更多时候会以只读、只写的方式来操作文件。
# r+: 可读写文件，文件不存在就会报错
#w+: 先写再读，文件存在就重新编辑文件，不存在则创建新文件
# f = open('test.txt','w+')
# #print(f.read())
# f.write("hello python")   #重新编辑文件内容，原先内容清空了。
# print(f.read())           #没有读取出来，涉及光标，写完之后光标在文件内容后面，读取是从光标以后开始读，所以读取出来是空白
# f.close()

#2.4.4. a:  追加模式，不存在则创建新文件进行写入，存在则在文件原有内容的基础上添加新的内容，也就是说，新的内容将会被写入到已有内容之后。
# f = open('test.txt','a')   #a就是append的缩写，追加的意思
# #print(f.read())
# f.write("test is being written...")
# #print(f.read())  #不支持读操作
# f.close()
#注意改变光标的位置

#文件指针:文件指针标记从哪个位置开始读取数据。
# f = open('test.txt','w+')
# f.write("Hello BingBing")
# print(f.read())  #读取出来是空白
# f.close()

#第一种方式：再改为只读模式读取
# f = open('test.txt')
# #f.write("Hello BingBing")
# print(f.read())
# f.close()

#第二种方式:
# 2.5 文件定位操作--tell()和seek()
# tell(): 显示文件内的当前位置，即文件指针当前位置
# seek(offset,whence): 移动文件读取指针到指定位置
#offset:偏移量，表示要移动的字节数
#whence:起始位置，表示移动字节的参考位置，默认值是0，0代表将文件开头作为参考位置；1代表将当前位置作为参考位置，2代表将文件结尾作为参考位置
#注意: 现在只要记住seek(0,0)会将光标移到文件开头
# f = open('test.txt','w+')
# f.write('hello,DingDing')
# pos = f.tell()
# print('当前光标的位置:',pos)     # 14--文件内容长度
# #把光标移到文件开头
# f.seek(0,0)
# #print("现在光标的位置:",pos)     #两次光标的位置都是一样的
# #因为两次都是使用的pos
# pos2 = f.tell()
# print("第二次光标的位置:",pos2)
# print(f.read())
# f.close()

#3.1 with open
#作用:代码执行玩，系统会自动调用f.close(),可以省略文件关闭步骤
# with open('test.txt','w') as f:
#     f.write('emmm...')   #注意缩进！f是文件对象
# print(f.closed)     #True ---代表文件已关闭

# with open('test.txt','w') as f:
#     f.write('我是你爸爸')  #注意缩进！！！
# print(f.closed)     #True ---代表文件已关闭
# #乱码，因为写入中文字符时，文件编码格式为gbk,此时pycharm中的文件会将你输入的中文显示为16进制数，并会提示你用gbk编码reload文件。
# #这时候就要将GBK改成utf-8格式
# with open('test.txt','w',encoding = "utf-8") as f:
#     f.write("我是你爸爸")
# print(f.closed)

#with open('test01.txt') as f:
#报错，在文本文件中夹杂了一些非法编码的字符。
# with open('test01.txt',encoding="utf-8") as f:
#     print(f.read())

#案例：图片复制
"""
1.新建一个文件夹
2.读取图片，为什么要先读取图片？因为图片是一个二进制文件，想要写入二进制文件的话必须要先拿到
3.写入图片
"""
# import os
# desk = "C:\\Users\\1\\Desktop\\新建文件夹\\"
# #打开原文件并读取
# with open(desk+"鱼.png", "rb") as f:
#     img = f.read()
#     # print(img)
# # 将读取的内容写入到新文件夹中
# with open("D:\\python\\py_study\\鱼.png","wb") as f:
#     f.write(img)


#导入模块
import os     #导入os模块
#1.文件重命名: os.rename(旧名,新名)
#os.rename('test.txt','test02.txt')
#2.删除文件: os.remove
#os.remove('test02.txt')
#os.remove('D:\CodeWorkspace\pycharm\PythonStudy\study\test02.txt')
#3.创建文件夹: os.mkdir
#os.mkdir('zs')
#4.删除文件夹: os.rmdir
#os.rmdir('zs')
#5.获取当前目录: os.getcwd
#print(os.getcwd())
#6.获取目录列表 os.listdir
# print(os.listdir())     #获取当前目录的列表
# print(os.listdir('../'))#获取上一级目录的列表

