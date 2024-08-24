if __name__ == '__main__':
    #if语句
    if 1 > 0:
        print('hello world')
        print('1>0')
    print('hello world again')

    a = int(input("请输入一个数字"))
    print(a,type(a))

    #if...else语句
    if a > 0:
        print('这是一个大于零的数字')
    else:
        print('这是一个小于或者等于零的数字')
    #if..elif..else语句
    if a > 0:
        print('这是一个大于零的数字')
    elif a == 0:
        print('这是零')
    else:
        print('这是一个小于零的数字')
