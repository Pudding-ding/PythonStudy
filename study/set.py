if __name__ == '__main__':

    # 集合是个KEY，存储一些不重复的元素
    a = {'a', 'b', 'c'}

    b = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    print(type(a))

    t = 'd' in a
    print(t)

    x = 'a' in b
    print(x)

    l = [1, 2, 3, 2, 4, 5, 2]
    s1 = set(l)
    print(s1, type(s1), list(s1))

    s = {1, 2, 3, 4}

    s.add(5)
    print(s)

    s.remove(5)
    print(s)

    # 集合元素无序
    b = '12345'
    s2 = set(b)
    print(s2)
    s3 = {1, 2, 3, 4}
    s4 = {3, 4, 5, 6}
    print(s3 & s4)
    print(s3 | s4)
    print(s3 ^ s4)
    print(s3 - s4)
