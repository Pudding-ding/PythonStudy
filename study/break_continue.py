if __name__ == '__main__':
    #break

    for i in range(10):
        print(i)
        if i % 2 == 0:
            break
    #   if i % 2 ! == 0:余数
    #       break

    #continue
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
# 1 2 2 4 6 8
# range(x)-->[0,x)中的所有整数
#每个循环内部的变量都是局部变量，两个不嵌套的循环之间，变量是无关的