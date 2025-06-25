""""
# 560. 和为K的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列
"""""
# 法一：列举所有可能-----当然通过不了咯，时间复杂度高
def subarray_sum1(nums, k):
    count = 0
    n = len(nums)
    for start in range(n):
        total = 0
        for end in range(start, n):
            total += nums[end]
            if total == k:
                count += 1
    return count

# 前缀和--新概念--数组的前n项之和
def subarray_sum2(nums, k):
    from collections import defaultdict
    prefix_count = defaultdict(int)  # 定义出现频率表
    prefix_count[0] = 1  # 初始化：前缀和为0出现1次
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        # 检查当前前缀和减去k是否存在 → 有则表示存在一段和为k的子数组
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1  # 记录当前前缀和出现次数
    return count

if __name__ == "__main__":
    nums = list(map(int, input("请输入数组元素（空格分隔）: ").split()))
    k = int(input("请输入目标值 k："))
    print("该数组中和为 k 的子数组的个数：", subarray_sum1(nums, k))
    print("该数组中和为 k 的子数组的个数：", subarray_sum2(nums, k))
