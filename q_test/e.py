if __name__ == '__main__':
    a = 0
    for i in range(1, 1000, 2):
        a += i
    b = 0
    for i in range(0, 1001, 2):
        b += i
    d = {
        'jishu': a,
        'oushu': b
    }
    print(d)
    list = []
    for i in range(1,1001):
        list.append(i)
    print('list=', list)
