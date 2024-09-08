# 3. 字符串常见操作
# 3.1 查找
# 3.1.1 find()
# find():检查某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就返回-1
# find(子字符串，开始位置下标，结束位置下标)--位置范围包前不包后[开始位置下标，结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name1 = 'dingding'
print(name1.find('i'))     # 1--第一个i的下标为1
print(name1.find('ding'))  # 0--检测到第一个ding。d的下标为0
print(name1.find('d',3))  # 4
print(name1.find('d',5))  # -1--超出范围，不包含返回-1
print(name1.find('d',3,5))# 4--在下标3-5位置范围内查找
print(name1.find('d',3,4))# -1--包前不包后[3,4)


# 3.1.2 index()
# index():检查某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就报错
# index(子字符串，开始位置下标，结束位置下标)--位置范围包前不包后[开始位置下标，结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找; 和find的区别：find没找到返回-1，index没找到就报错
name2 = 'pudding'
print(name2.index('u'))     #1
print(name2.index('u',2))   #报错，从下标2开始找，没有找到
print(name2.index('u',1,3)) #1


# 3.1.2 count()
# count():返回某个子字符串在整个字符串中出出现的次数，没有就返回0
# count(子字符串，开始位置下标，结束位置下标)--位置范围包前不包后[开始位置下标，结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name3 = 'dingding'
print(name3.find('i'))     # 2--出现了两次i
print(name3.find('b'))     # 0--b没有出现过
print(name3.find('d',1))   # 1
print(name3.find('d',1,3)) # 0--在下标1-3位置范围内查找
print(name3.find('d',1,4)) # 1--包前不包后[1,4)


# 3.2 判断
# 3.2.1 startwith()
# startwith():是否以某个子字符串开头，是的话就返回True,不是的话就返回False，如果设置了开始和结束位置下标则在指定范围内检查
# startwith(子字符串，开始位置下标，结束位置下标)
st1 = 'sixstar'
print(st1.startswith('s'))     # True
print(st1.startswith('six'))   # True
print(st1.startswith('sex'))   # False
print(st1.startswith('s',2,6)) # False


# 3.2.2 endwith()
# endwith():是否以某个子字符串结尾，是的话就返回True,不是的话就返回False，如果设置了开始和结束位置下标则在指定范围内检查
# endwith(子字符串，开始位置下标，结束位置下标)
st2 = 'sixstar'
print(st2.endwith('er'))   # False

# 3.2.3 isupper()
# isupper():检测字符串中所有字母是否都为大写，是的话就返回True,不是的话就返回False
st3 = 'sixstar'
print(st3.isupper())    #False
print('SIX'.islower())  #True


# 3.3 修改元素
# 3.3.1 replace()：替换
# replace(旧内容，新内容，替换次数)
#注意：替换次数可以省略，默认全部替换
re = 'dingding'
print(re.replace('d','j'))    #jingjing
print(re.replace('d','j',1))  #jingding


# 3.3.2 split()：指定分隔符来切字符串
# split(‘分割符号’，分割次数)
#注意：分割次数可以省略，默认全部分割，如果字符串中不包含分割内容，就不进行分割，会作为一个整体
sp = 'hello,python'
print(sp.split(','))  #['hello','python']--以列表的形式返回
print(sp.split('d'))  #['hello,python']--字符串中不包含d
print(sp.split('o'))  #['hell','pyth','n']
print(sp.split('o',1))#['hell','python']--指定只分割一次


# 3.3.3 capitalize():第一个字符大写,其他都小写
ca = 'dingding'
print(ca.capitalize())  #Dingding


# 3.3.4 lower():大写字母转为小写
lo = 'dINgdiNg'
print(lo.lower())  #dingding


# 3.3.5 upper():小写字母转为大写
up = 'dINgdiNg'
print(up.upper())  #DINGDING