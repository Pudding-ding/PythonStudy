""""
# 41.缺失的第一个正数
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""""

# 法一：将正数n放到索引n-1的位置，然后遍历
def first_missing_positive1(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:   # 把 nums[i] 放到正确的位置
            # 交换 nums[i] 和 nums[nums[i] - 1]
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    for i in range(n):     # 查找第一个不符合连续排序的位置
        if nums[i] != i + 1:
            return i + 1
    return n + 1

# 利用集合----超时！
def first_missing_positive2(nums):
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i

if __name__ == "__main__":
    nums = list(map(int, input("请输入整数数组（空格分隔）：").split()))
    # print("缺失的最小正整数为：", first_missing_positive1(nums))
    # print("缺失的最小正整数为：", first_missing_positive2(nums))
