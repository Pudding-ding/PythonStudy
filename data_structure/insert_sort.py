def insert_sort(li):
    for i in range(1, len(li)): #i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1   #j指的是手里牌的下标
        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)

li = [3,4,1,5,9,7,8,6]
print(li)
insert_sort(li)
