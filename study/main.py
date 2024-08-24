if __name__ == '__main__':
    a = [1, 2, 3]

    b = [1, 'abc', 2.0, ['a', 'b', 'c']]

    print(a)
    print(b)

    print(a[0], a[1], sep='-')

    c = b[1:3] #1和3-1

    print(c, type(c))
