if __name__ == '__main__':
    # 控制台打等边三角图像
    num = int(input("请输入你想要的行数："))
    i = 1
    b = num
    while i <= num:
        if i <= b:
           print(' ' * (b - i) + '*' * (2 * i - 1) + ' ' * (b - i))
        print()
        i += 1
