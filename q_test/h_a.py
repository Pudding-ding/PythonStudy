if __name__ == '__main__':
    n = 2
    l = []
    while n > 0:
        l.append(input("请输入任意两串字符串："))
        n -= 1

    ms = l[0]#注意while循环的位置
    ss = l[1]
    n = len(ms)
    m = len(ss)
    i = j = 0
    while i < n and j < m:
        if ms[i] == ss[j]:
            i += 1
            j += 1
        else:
            i += 1
            j = 0
    if j == m:
        print(i - j)
    else:
        print('-1')
        # for i in ms:
        #     for j in ss:
        #         if i == j:
        #             ms.index(i) += 1
        #             ss.index(j) += 1
