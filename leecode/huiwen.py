def all_ss(s:str):
    # 1 <= s.length <= 1000
    # s= input("随机长度字符串")
    ms = list(s)
    ss_l = []
    ss = ''
    alss = []
    for a in range(0,len(ms)):
        for i in range(0,len(ms) - a):
            ss_l.append(ms[i:i + (a + 1)])#增加好几个元素组成的一个字符串
            for j in ss_l:
                ss += j
                alss.append(ss)
    return alss

def huiwen(ss):
    lss = list(ss)
    lss.reverse()
    rss = ''
    for j in lss:
        rss += j
    if rss == ss:
        return True
    else:
        return False

def longest(li):
    longest_s = li[0]
    for i in li:
        if len(i) > len(longest_s):
            longest_s = i
    return i

if __name__ == '__main__':
    s = input('请输入随机长度字符串：')
    alss = all_ss(s = s)
    longest_hs = []
    for item in alss:
        result = huiwen(ss = item)
        if result == True:
            longest_hs.append(item)
            print(longest(li = longest_hs))


# def testHuiwen():
#     print(huiwen("asdfafdsa"))

def testAll_ss():
    print(all_ss('12345'))

# def testLongst():
#     print(longest(li=['a', 'as', 'asd']))
