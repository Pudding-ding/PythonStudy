def myReverse(ss:str) :
    s1 = list(ss)    # 这里是值复制，对s1 进行的操作，不会同步到 s1上
    s2 = []
    index = len(s1)
    while index > 0:
        index -= 1
        s2.append(s1[index])
    s3 = ''
    for x in s2 :
      s3 += x
    return s3

if __name__ == '__main__':
    print(myReverse('asd'))
