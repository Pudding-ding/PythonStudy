if __name__ == '__main__':
    s = list(input("输入dingding"))
    for i in s:
        if i == 'd':
            s[s.index(i)] = 'j'
            # i的意思就只是一个临时变量，每一次存换就把s的指定位置的值，复制到i身上所以要找索引
    print(s)
    for i in s:
        print(i,end='')
