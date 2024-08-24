if __name__ == '__main__':
    # a = [1, 2, 3, 4]
    #
    # print(max(a))

    def demo():
        print('hello world')
        print('demo')
    demo()

    def demo1(a, b):
        print(a,b)
    demo1(a=[1,2,3],b={1: 1,2: 2})

    def sum(a, b):
        return a + b
    sum([1,2,3],[4,5,6])#关键字参数or位置参数

    def my_max(a):
        if not a:
            return None
        max_value = a[0]
        for item in a:
            if item > max_value:
                max_value = item
        return max_value
    a = [1,4,5,2,3,8,10]
    print(my_max(a))
