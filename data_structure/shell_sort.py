def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):  # i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap # j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j = j - gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li)//2
    while d >= 1:
        insert_sort_gap(li,d)
        d //= 2

li = list(range(1000))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)
