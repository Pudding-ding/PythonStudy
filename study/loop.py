if __name__ == '__main__':
    # while
    a = 10

    while a > 0:
        print(a)
        a = a - 1

    print('结束')

    # for
    b = '12345'

    c = ('a', 'b', 'c', 'd')

    d = [1, 2, 3, 4]

    e = {
        1: 'a',
        2: 'b',
        3: 'c'
    }

    for item in e.items():
        print(item)

    for item in range(0, 21, 2):
        # 1-20的步长4
        print(item)
