if __name__ == '__main__':
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
