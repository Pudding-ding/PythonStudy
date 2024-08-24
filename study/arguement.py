if __name__ == '__main__':
    def add(a, b):
        return a + b
    print (add(1, 2))

    #加很多数怎么办？，无限制传参
    def add (*args):
        # print(args)
        result = 0
        for item in args:
            result += item
        return result

    print (add(1,2,10,20,30))
    #参数是可变了，那怎么有关键字呢

    def add(**kwargs):
        # print(kwargs)   出一个字典
        return ((kwargs.get('a')+ kwargs.get('b'))* kwargs.get('c'))
    print(add(a=1, b=2, c=3))

    def tt(a, b, c):
        print(a + b + c)
    def add(x, **kwargs):
        if x == 2:
            tt(**kwargs)
    add(x = 2, a = 1, b = 2, c = 2)

    def tt1(a, b = False):#正常参数要放前面
        if b:
            return a
        else:
            return a * a
    print(tt1(a=2,b=True))
