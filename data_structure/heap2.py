import heapq  #q->queue 优先队列
import random

li = list(range(1,100))
random.shuffle(li)

print(li)

heapq.heapify(li)  # 建堆--建的小根堆

n = len(li)
for i in range(n):
    print(heapq.heappop(li), end=',')


