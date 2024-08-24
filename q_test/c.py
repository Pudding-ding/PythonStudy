if __name__ == '__main__':
    # 控制台打等边三角图像
    num = int(input("请输入你想要的行数："))
    i = 1
    while i <= num:
        a = 1
        b = 1
        while b <= num - i:
            print(' ',end='')
            b += 1
        while a <= 2 * i - 1:
            print('*',end='')
            a += 1
        print()
        i += 1
