if __name__ == '__main__':
    a = 22
    while True:
        b = int(input("请输入一个0-100之间的数字："))
        if b == a:
            print("你猜对啦")
            break
        elif b > a:
            print("猜小点")
        else:
            print("猜大点")

# import random
# a = random.randint(0, 100)
