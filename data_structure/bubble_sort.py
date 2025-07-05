import random
from cal_time import *

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):  #第一趟
        exchange = False
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j] #交换
                exchange = True
        # print(li)
        if not exchange:
            return


# li = list(range(10000))
# random.shuffle(li)

# print(li)
# bubble_sort(li)
# print(li)

# li = [3,2,4,5,8,7,6,9,1]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li)
bubble_sort(li)
