if __name__ == '__main__':
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
