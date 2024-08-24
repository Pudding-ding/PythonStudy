if __name__ == '__main__':
    # 控制台打菱形图像
    a = int(input("请输入任意大于1的奇数："))
    num = a // 2 + 1
    i = 1
    n = 1
    m = num
    while (n * i) <= m:
        b = 1
        if i == num:
            n = -1
            m = -1
        while b < (num * 2 + 1):
            if b <= (num - i) or b >= (num + i):
                print(' ',end='')
            else:
                print('*',end='')
            b += 1
        print()
        i += n
