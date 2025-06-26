""""
# 239. 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
"""""

# 法一：每次窗口滑过来就取最大值--通过不了
def max_sliding_window1(nums, k):
    res =[]
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        res.append(max(window))
    return res

# 法二：窗口往前滑动，如果下一个数字大于已有的数字，就进入队列，然后移除其他小于这个元素的值，就是一直保持窗口中的数字是已经滑动过来的最大数字
from collections import deque
def max_sliding_window2(nums, k):
    res = []
    q = deque() # deque用来储存元素的索引
    for i in range(len(nums)):
        while q and nums[i] > nums[q[-1]]:  # 移除队尾所有小于当前元素值
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()   # 移除窗口外的索引
        if i >= k - 1:
            res.append(nums[i])
    return res

if __name__ == "__main__":
    nums = list(map(int, input("请输入一串数（仅空格分隔）：").split()))
    k = int(input("请输入窗口大小 k："))
    print("输出：", max_sliding_window1(nums, k))
    # print("输出：", max_sliding_window2(nums, k))
