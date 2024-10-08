from threading import Thread,Lock   # 导入线程模块
import time
# 19.线程续课
# 1.1 线程之间共享资源(全局变量)
# li = []   # 全局变量
# # 写入数据
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.2)
#     print("写入的数据是:", li)
# # 读取数据
# def rdata():
#     print("读取的数据是：", li)
# if __name__ == "__main__":
#     # 创建子线程
#     t1 = Thread(target=wdata)
#     t2 = Thread(target=rdata)
#     # 开启子线程
#     t1.start()
#     # 阻塞线程
#     # t1.join()   # 加了join()就会等待t1任务执行结束
#     time.sleep(1)
#     t2.start()
#     # t2.join()

# 1.2 资源竞争
# a = 0
# b = 1000000
# # 循环一次就给全局变量a+1
# def add():
#     for i in range(b):
#         global a
#         a += 1
#     print("第一次:",a)
#
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print("第二次:",a)
# # add()      # 第一次: 1000000
# # add2()     # 第二次: 2000000
# if __name__ == "__main__":
#     first = Thread(target=add)
#     second = Thread(target=add2)
#     first.start()
#     second.start()

# 2.线程同步
# 2.1两种方式： join 和互斥锁
# 2.2 互斥锁
# 2.2.1 acquire() 加锁
# 2.2.2 release() 解锁
# 两个方法必须要成对出现，否则容易形成死锁
# 死锁: 一直等待对方释放锁的情景
# 死锁会造成应用程序停止响应，不再处理其他任务
# a = 0
# b = 1000000
# # 1.创建互斥锁
# lock = Lock()
# # 循环一次就给全局变量a+1
# def add():
#     lock.acquire()    # 上锁
#     for i in range(b):
#         global a
#         a += 1
#     print("第一次:",a)
#     lock.release()   # 解锁
#
# def add2():
#     lock.acquire()   # 上锁
#     for i in range(b):
#         global a
#         a += 1
#     print("第二次:",a)
#     lock.release()  # 解锁
# # add()      # 第一次: 1000000
# # add2()     # 第二次: 2000000
# if __name__ == "__main__":
#     first = Thread(target=add)
#     second = Thread(target=add2)
#     first.start()
#     # first.join()  # 等待第一个子线程执行完成以后，代码再继续往下执行，开始执行第二个子线程
#     second.start()
# 注意，互斥锁是多个线程一起去抢，抢到锁的线程先执行。