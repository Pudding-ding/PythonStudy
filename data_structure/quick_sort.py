import random
import copy

from cal_time import *
from data_structure.bubble_sort import bubble_sort


def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:   #从右面找比tmp小的数
            right -= 1       #往左走一步
        li[left] = li[right]  #把右边的值写到左边的空位上
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]  #把左边的值写到右边的空位上
    li[left] = tmp   #把tmp归位
    return left


# def quick_sort(li,left,right):
#     if left < right:
#         mid = partition(li,left,right)  #partition算出中间的下标位置
#         quick_sort(li, left, mid-1)
#         quick_sort(li, mid+1, right)
#
# li = [5,7,4,6,3,1,2,9,8]
# quick_sort(li,0,len(li)-1)
# print(li)

def _quick_sort(li,left,right):
    if left < right:
        mid = partition(li,left,right)  #partition算出中间的下标位置
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

li = list(range(10000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

quick_sort(li1)
bubble_sort(li2)

print(li1)
print(li2)