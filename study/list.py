if __name__ == '__main__':
    #4.列表
    #基本格式：列表名 = [元素1,元素2,元素3..]
    #注意：
    #所有元素放在[]中，元素与元素之间用，隔开
    #元素之间的数据类型可以各不相同
    li = [1,2,'a',4]
    print(li,type(li))  # [1,2,'a',4] <class 'list'>
    #列表也可以进行切片操作
    print(li[0:3])      #[1,2,'a']
    #列表也是可迭代对象，可以for循环遍历取值
    for i in li:
        print(i)        #1换行2换行a换行4


    #4.1列表的添加
    # append()--整体添加
    # extend()--分散添加，将另外一个类型中的元素逐一添加   且要为可迭代对象如果li.extend(4)就会报错
    # insert()--在指定位置插入元素，指定位置若有元素，原有元素就会后移
    li1 = ['one','two','three']
    li1.append('four')      #['one', 'two', 'three', 'four']--append整体添加
    #  ???为什么直接print(li1.append('four'))出来结果是None???
    li1.extend('four')      #['one', 'two', 'three','four', 'f', 'o', 'u', 'r']--extend分散添加，将另外一个类型中的元素逐一添加
    li1.insert(2,'five')    #['one', 'two', 'five', 'three', 'four', 'f', 'o', 'u', 'r']--insert在指定位置插入元素，指定位置若有元素，原有元素就会后移


    #4.2列表的修改
    #直接通过下标修改即可
    li2 = [1,2,3]
    li2[1] = 'a'
    print(li2)


    #4.3查找元素
    #in:判断指定元素是否存在列表中，如果存在就返回Ture,不存在就返回False
    #not in:判断指定元素是否存在列表中，如果不存在就返回Ture,存在就返回False
    #index:返回指定数据的下标，如果查找数据不存在会报错--跟字符串中的用法相同
    #count：统计指定数据在当前列表中出现的次数--跟字符串中的用法相同
    li3 = ['a','b','c','d']
    print('b' in li3)       #Ture
    print('b' not in li3)   #False

    #案例：用户输入昵称，昵称重复则不能使用
    #定义一个列表，保存已经存在的昵称
    name_list = ['dingding','qiaoqiao','jingjing']
    while True:
        name = input('请输入您的昵称')
        #判断昵称是否已经存在
        if name in name_list:
            print(f'您输入的昵称{name}已经存在了哦')
        else:
            print(f'昵称{name}已经被您使用')
            #把昵称新增到列表
            name_list.append(name)
            print(name_list)
            break


    #4.4删除元素
    #4.4.1 del
    li4 = ['a','b','c','d','e']
    #del li4     #删除列表
    del li4[0]  #['b','c','d','e']--根据下标删除

    #4.4.2 pop:删除指定下标的数据，python3版本默认删除最后一位
    li4.pop()   #['b','c','d']--默认删除最后一位
    li4.pop(1)  #['b','d']--不能指定元素删除，只能根据下标进行删除，下标不能超出范围

    #4.4.3 remove：根据元素的值进行删除,列表中不存在该元素时会报错，若含有多个该元素，默认仅删除最开始出现的
    li4.remove('d')  #['b']


    #4.5 列表的排序
    #sort:将列表按从小到大的顺序排列
    #reverse:倒序，将列表倒置（反过来）
    li5 = [1,3,4,8,5,6]
    li5.sort()  #[1,3,4,5,6,8]
    li5.reverse()  #[6,5,8,4,3,1]


    #4.6 列表推导式
    #4.6.1格式一：[表达式 for 变量 in 列表]
    #注意：in后面不仅可以放列表，还可以放range(),可迭代对象
    li6 = [1,2,3,4,5,6]
    [print(i*5) for i in li6]   #前面的i是表达式，后面的i是元素
    #把1-5放进列表里面
    li61 = []
    #for i in range(1,6):
        #li61.append(i)
    # print(li61)
    [li61.append(i) for i in range(1,6)]
    print('range(0,6)-->[0,6)中的所有整数')
    print(li61)   #与88-90行注释部分效果一样

    #4.6.2格式二：[表达式 for 变量 in 列表 if 条件]
    #把奇数放进列表里面
    li62 = []
    # for i in range(1,11):
    #     if i % 2 == 1:
    #         li62.append(i)
    # print(li62)
    [li62.append(i) for i in range(1,11) if i % 2 == 1]
    print(li62)    #与97-100行注释部分效果一样


    #4.7列表嵌套
    #含义：一个列表里面又有一个列表
    li7 = [1,2,3,[4,5,6]]  #[4,5,6]是里面的列表
    print(li7[3])          #取出里面的列表
    print(li7[3][2])       #取出内列表中下标为2的元素



    #eg:
    list1 = [9, 1, -4, 3, 7, 11, 3]

    print('list1的长度=', len(list1))

    print('list1的最大值=', max(list1))

    print('list1的最小值=', min(list1))

    print('list=里3这个元素一共出现了{}次'. format(list1.count(3)))
    #列表的改变

    list2 = ['a', 'c', 'd']

    #给它结尾加'e'

    list2.append('e')
    print('list2=',list2)

    #在ac之间插入b

    list2.insert(1, 'b')
    print('list2=',list2)

    #删除b

    list2.remove(list2[1])
    print('list2=',list2)

    #改要类型一致
    list2[0] = '1'
    print('list2=',list2)

    #翻转
    list3 = ['a', 'b', 'c']
    list3.reverse()
    print('list3=',list3)

    #排序
    list4 = [9, 1, -4, 3, 7, 11, 3]
    list4.sort()#正
    print('list4=',list4)

    list4.sort(reverse=True)#反
    print('list4=',list4)
    print(list4.index(list4[0]))
