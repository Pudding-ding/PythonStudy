def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for val in li:
        i = min(val // (max_num // n), n-1)  # i 表示val放到几号桶里
        buckets[i].append(val)  # 把val加到桶里面
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

import random
li = [random.randint(0, 10000) for _ in range(100000)]
print(li)
print(bucket_sort(li))