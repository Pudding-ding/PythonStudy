from cal_time import *

@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

@cal_time
def binary_search(li, val):
    left, right = 0, len(li)-1
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: #待查找的值在mid左侧
            right = mid - 1
        else:               #待查找的值在mid左侧
            left = mid + 1
    else:
        return None

li = list(range(10000))
print(linear_search(li, 3890))
print(binary_search(li, 3890))