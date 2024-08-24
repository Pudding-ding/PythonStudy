if __name__ == '__main__':
    s = list(input("请输入你想要的字符串："))
    print(s)
    for i in s:
        print ("序号：%s   值：%s" % (s.index(i) + 1, i))
