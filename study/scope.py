if __name__ == '__main__':
    x = 1
    x += 1
    print(x)
    def demo():
        x = 10
        a = 11
        a = a + x
        print(a)
        print(x)

    demo()
    print(x)


    def demo(a):
        a = a + 10
        print(a)

    demo(a=x)
    print(x)#只是把x的值传进去了

    y = [1,2,3]
    print(y)
    def demo1(a):
        a = a+[4]
        # a.appemd(4)
        print(a)


    z = 1
    def demo2(a):
        global z
        # 把z当全局变量去使用
        z = z + a
        print (z)
    demo2(a=10)
    print(z)
