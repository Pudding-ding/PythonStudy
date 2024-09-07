if __name__ == '__main__':
    #5.元组
    #5.1  基本格式：元组名 = (元素1,元素2,元素3..)
    #注意：
    #所有元素放在()中，元素与元素之间用,隔开
    #元素之间的数据类型可以各不相同
    #只有一个元素的时候，末尾必须加上,否则返回唯一的值的数据类型
    #与列表的区别：
        # 1.元组只有一个元素时末尾必须加,列表不需要
        # 2.元组只支持查询操作，不支持增删改操作，其余操作与列表相同

    #5.2 元组的应用场景
    #函数的参数和返回值

    #格式化输出后面的（）本质上就是一个元组
    name1 = 'dingding'
    age = 21
    print('%s的年龄是：%d' % (name1, age))
    info = (name1, age)
    print(type(info))
    print('%s的年龄是：%d' % info)

    #数据不可以修改，保护数据


    #eg:
    li = [1,2,'a',4]

    # 元组创建

    a = (1, 2, 3)

    b = [1, 2, 3],

    print(a, type(a))
    print(b, type(b))

    # 元组访问

    print(a[1])
    print(a[1:])
    print(a[-1])

    # 获取元组的一些基本信息
    tuple1 = (9, 1, -4, 3, 7, 11, 3)

    print('tuple1的长度=', len(tuple1))

    print('tuple1的最大值=', max(tuple1))

    print('tuple1的最小值=', min(tuple1))

    print('tuple1里3这个元素一共出现了{}次'. format(tuple1.count(3)))

    # 元组元素不能变
    print(tuple1.index(9))
