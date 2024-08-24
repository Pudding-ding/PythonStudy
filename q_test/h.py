if __name__ == '__main__':
    n = 2
    l = []
    while n > 0:
        l.append(input("请输入任意两串字符串："))
        n -= 1

    s = list(set(l[0]) & set(l[1]))
    # 这行代码，因为set是无序的，所以s的内容虽然固定是 bfg，但是顺序每一次都是不一样的，因此可能会出现 s == list(l[1])的情况
    if s == list(l[1]):
        # 两个列表内容和顺序，必须完全一样，才能算对等
        print(l[0].index(s[0]))
    else:
        print('-1')
