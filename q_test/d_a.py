if __name__ == '__main__':
    num= int(input("请输入任意大于1的数字："))
    i = 1
    n = 1
    m = num
    while (n * i) <= m:
        b = 1
        while b < (num * 2 + 1):
            if b <= (num - i) or b >= (num + i):
                print(' ',end='')
            else:
                print('*',end='')
            b += 1
        print()
        i += n
        if i == num:
            n = -1
            m = -1
