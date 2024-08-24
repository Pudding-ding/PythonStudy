if __name__ == '__main__':
    a = int(input("请输入大于1的一个奇数："))
    b = a//2+1
    i = 1
    while i <= a:
        if i <= b:
            print(' '*(b - i) + '*' *(a - 2*(b - i)) + ' '*(b - i))
        else:
            print(' '*(i - b) + '*' *(a - 2*(i - b)) + ' '*(i - b))
        i += 1
