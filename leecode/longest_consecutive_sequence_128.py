""""
128.最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""""

# 使用集合消除重复数据,从每个连续序列的起点开始向右寻找
def longest_consecutive1(nums):
    num_set = set(nums)
    max_len = 0
    for num in num_set:
        if num - 1 not in num_set:  # 判断起点
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            max_len = max(max_len, streak)
    return max_len

# 先对数组中的所有数据进行排序，再判断其是否连续
def longest_consecutive2(nums):
    if not nums:
        return 0
    nums = sorted(set(nums))  # 排序并去重
    max_len = 1
    current_len = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1  # 断了就重新开始
    return max_len

if __name__ == '__main__':
    raw = input('请输入整数序列如：2, 3, 4, 6：')
    # 防止输入非法字符，正确转换为整数列表
    nums = []
    for x in raw.split(','):
        x = x.strip()
        if x.lstrip('-').isdigit():  # 支持负数
            nums.append(int(x))
    print("长度 =", longest_consecutive1(nums))
    print("长度 =", longest_consecutive2(nums))

