if __name__ == '__main__':
    #6.字典
    #6.1  基本格式：字典名 = {键1:值1,键2:值2,键3:值3..}
    #注意：
    #键值对形式保存，键和值之间用:隔开，每个键值对之间用,隔开
    #dic = {'name':'dingding','age':'22'}
    #字典中的键具有唯一性，但是值可以重复
    #dic2 = {'name': 'dingding', 'name': 'qiaoqiao'}--不会报错，键名重复前面的值会被后面的值覆盖
    #dic3 = {'name': 'dingding', 'name2': 'dingding'}


    #6.2 字典常见操作一
    #6.2.1 查看元素
    #变量名.get(键名)
    dic1 = {'name':'dingding','age':'22'}
    print(dic1['name']) #print(dic[2])会报错--不可以根据下标，字典中没有下标，查找元素需要根据键名
    #print(dic1['sex'])--键名不存在时也会报错
    print(dic1.get('tel'))            #None--键名不存在，返回None
    print(dic1.get('tel','不存在'))    #不存在--如果没有这个键名，返回自己设置的默认值

    #6.2.2 修改元素
    #变量名[键名] = 值
    dic2 = {'name': 'dingding', 'age': '22'}
    dic2['name'] = 'qiaoqiao'  # 列表通过下标修改，字典通过键名修改

    #6.2.3 添加元素
    #变量名[键名] = 值
    #键名存在就修改，不存在就新增
    dic3 = {'name': 'dingding', 'age': '22'}
    dic3['name'] = 'qiaoqiao'
    print(dic3)       #{'name': 'qiaoqiao', 'age': '22'}
    dic3['sex'] = 'girl'
    print(dic3)       #{'name': 'qiaoqiao', 'age': '22','sex':'girl'}

    #6.2.4 删除元素

    #del：删除整个字典--del 字典名
    dic41 = {'name': 'dingding', 'age': '22'}
    del dic41
    #print(dic41)  #报错--已经被删除了，找不到这个字典
    # #删除指定键值对，键名不存在就会报错--del 字典名[键名]
    dic411 = {'name': 'dingding', 'age': '22'}
    del dic411['name']
    print(dic411)  #{ 'age': '22'}

    #clear()清空整个字典里面的东西。但保留了这个字典
    dic42 = {'name': 'dingding', 'age': '22'}
    dic42.clear()
    print(dic42)  #{}

    #pop()删除指定键值对，键不存在就会报错
    dic43 = {'name': 'dingding', 'age': '22'}
    dic43.pop('age')   # {'name': 'dingding'}
    # dic43.pop('sex')   #报错--不存在键名
    # dic43.pop()        #报错--没有指定键名
    dic43.popitem()    #3.7之后版本默认删除最后一个，之前删除随机一个


    #6.3 字典的常见操作二

    #6.3.1 len()：求长度
    dic = {'name': 'dingding', 'age': '22','sex':'girl'}
    print(len(dic))  #3--字典中有三个键值对
    li = [1,2,3,4]
    print(len(li))
    st = 'hello'
    print(len(st))

    #6.3.2
    # keys():返回字典里面包含的所有键名
    # values():返回字典里面包含的所有键名
    # items():返回字典里面包含的所有键值对，键值对以元组形式
    print(dic.keys())   #dict_keys(['name','age','sex'])
    print(dic.values()) #dict_values(['dingding','22','girl'])
    print(dic.items())  #dict_items([('name':'dingding'), ('age': '22'),('sex':'girl')])
    #for 循环取出键名和值
    for i in dic:
        print(i)  #只取出键名name换行age
    for j in dic.values():
        print(j)
    for k in dic.items():
        print(k)


    #6.4字典的应用场景
    #使用键值对，存储描述一个物体的相关信息


    #eg:
    #字典KEY是不可改变的数据类型
    e = dict(a=1,b=2,c='a')
    print(e)
    #字典的改变
    e['d'] = 123
    e['c'] = 3
    print(e)

    d = {
        'Name': 'Jack',
        'Age': 9,
        'Grade': 5,
    }

    print(d['Name'])
    print(d.get('name'))
    print(d.keys())
    print(d.values())
    print(d.items())

    c = d.pop('Name')

    print(c)

    print(d)

    d.clear()
    print(d)

    #字典的更新

    c = {
        1: 1,
        2: 2
    }
    c[3] = 3
    c[4] = 4
    print(c)

    d = {
        1: 5,
        6: 6
    }
    c.update(d)
    print(c)

    #e = {**c, **d}
    #print(e)
