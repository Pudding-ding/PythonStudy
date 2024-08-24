def myReverse(ss:str) :
    s1 = list(ss)    # 这里是值复制，对s1 进行的操作，不会同步到 s1上
    s1.reverse()
    s2 = ""
    for x in s1 :
      s2 += x
    return s2
    # for item in l:
    #     return item  # ?????

if __name__ == '__main__':
    print(myReverse('asd'))
