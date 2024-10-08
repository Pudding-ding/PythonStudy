import time
from multiprocessing import Process,Queue
import os
# from queue import Queue
# 20.进程
# 1.1 含义
# 是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础。
# 一个正在运行的程序或者软件就是一个进程
# 程序跑起来就成了进程
# 注意: 进程里面可以创建多个线程，多进程也可以完成多任务
# 1.2 进程的状态
# 1.就绪状态: 运行的条件都已经满足，正在等待cpu执行
# 2.执行状态: cpu正在执行其功能
# 3.等待(阻塞)状态： 等待某些条件满足，如一个程序sleep了，此时就处于等待状态
# print("我是丁丁")   # 程序开始，处于执行状态
# sex = input("输入性别:")  # 光标闪动，等待用户输入，处于等待状态
# print(sex)         # 执行状态
# time.sleep(1)      # 延时1秒，等待(阻塞)状态

# 2.进程语法结构
# multiprocessing模块提供了Process类代表进程对象
# 2.1 Process 类参数
# 1.target:执行的目标任务名，即子进程要执行的任务
# 2.args: 以元组的形式传参
# 3.kwargs: 以字典的形式传参
# 2.2 常用的方法
# 1.start(): 开启子进程
# 2.is_alive(): 判断子进程是否还活着，存活返回True,死亡返回False
# 3.join(): 主进程等待子进程执行结束
# 2.3 常用的属性
# name: 当前进程的别名。默认Process-N
# pid: 当前进程的进程编号
# def sing():
#     # os.getpid():获取当前进程编号
#     # os.getppid(): 获取当前父进程编号
#     print(f"sing子进程编号:{os.getpid()}，父进程pid:{os.getppid()}")    # 父进程的pid就是py文件主进程的pid
#     print("唱歌")
# def dance():
#     print(f"dance子进程编号:{os.getpid()}，父进程pid:{os.getppid()}")
#     print("跳舞")
# if __name__ == "__main__":
#     # 创建子进程
#     # 修改子进程名第一种方式
#     p1 = Process(target=sing, name="子进程一")
#     p2 = Process(target=dance, name="子进程二")
#     # 开启
#     p1.start()
#     p2.start()
#     # 修改子进程名第二种方式
#     p1.name = "子进程1"
#     p2.name = "子进程2"
#     # 访问name属性
#     print("p1:",p1.name)
#     print("p2:",p2.name)
#     # 查看子进程的进程编号
#     print("p1.pid:",p1.pid)
#     print("p2.pid:",p2.pid)
#     print(f"主进程pid:{os.getpid()},主进程的父进程pid:{os.getppid()}",)
#     # cmd命令提示符窗口输入tasklist可以查看电脑里面进程的命令
#     # Ctrl+F 查找
#     # pycharm64软件进程编号就是主进程的父进程编号
# def eat(name):
#     print(f"{name}在干饭")
# def sleep(name):
#     print(f"{name}在睡觉")
# if __name__ == '__main__':
#     p1 = Process(target=eat,args=('bingbing',))
#     p2 = Process(target=sleep,args=('ziyi',))
#     p1.start()
#     p1.join()  # 主进程处于等待的状态，p1是运行状态
#     p2.start()
#     p2.join()
#     print("p1存活状态：",p1.is_alive())
#     print("p2存活状态：",p2.is_alive())
# 写在主进程中判断存活状态的时候需要加入join阻塞一下

# 2.4 进程间不共享全局变量
# li = []
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.2)
#     print("写入的数据是:", li)
# # 读取数据
# def rdata():
#     print("读取的数据是：", li)
# # 1.防止别人导入文件的时候执行main里面的方法
# # 2.防止windows系统递归创建子进程
# if __name__ == "__main__":
#     p1 = Process(target=wdata)
#     p2 = Process(target=rdata)
#     p1.start()
#     p1.join()
#     p2.start()
# 读取一直是空的，进程不共享全局变量

# 3.进程间的通信
# Queue(队列)
# q.put():     放入数据
# q.get():     取出数据
# q.empty(): 判断队列是否为空
# q.qsize():  返回当前队列包含的消息数量
# q.full():     判断队列是否满了
# 初始化一个队列队形
# q = Queue(3)   # 最多可以接收三条消息，没写或者是负值就代表没有上限，直到内存的尽头
# q.put("爱你到老")
# q.put("你在做梦")
# print("是否满了",q.full())
# q.put("年轻人不讲武德")
# print("是否满了2",q.full())
# # print(q.qsize())
# print(q.get())   # 获取队列的一条消息，然后将其从队列中移除
# print(q.get())
# print(q.empty())
# print(q.get())
# # print(q.empty())
# # print(q.qsize())
# li = ['张三','李四','王麻子','赵六']
# def wdata(q1):
#     for i in range(5):
#         print(f"{i}已经被放入")
#         q1.put(i)
#         time.sleep(0.2)
#     print("写入的数据是:", li)
# # 读取数据
# def rdata(q2):
#     while True:
#         # 判断是否为空，队列为空就退出循环
#         if q2.empty():
#             break
#         else:
#             print("取出数据:",q2.get())
#     print("读取的数据是：", li)
# 1.防止别人导入文件的时候执行main里面的方法
# 2.防止windows系统递归创建子进程
if __name__ == "__main__":
    # 创建队列对象
    q = Queue()
    p1 = Process(target=wdata,args=(q,))
    p2 = Process(target=rdata,args=(q,))
    p1.start()
    p1.join()     # 等待队列中的数据放入完成
    p2.start()