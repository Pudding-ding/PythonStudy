if __name__ == '__main__':
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
