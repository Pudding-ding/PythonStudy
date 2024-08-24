if __name__ == '__main__':
    # 控制台打图像
    num = int(input("请输入你想要的行数："))
    i = 1
    while i <= num:
        a = 1
        while a <= i:
            print("*",end='')
            a += 1
        print()
        i += 1
