""""
# 55.最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
"""""

def max_sub_array_kadane(nums):
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])   # 如果当前数本身更大，说明前面已经不连续--从i开始新子串
        max_sum = max(max_sum, current_sum)   # 更新最大值
    return max_sum


if __name__ == "__main__":
    nums = list(map(int, input("请输入一串数（仅空格分隔）：").split()))
    print("最大子数组和为：", max_sub_array_brute(nums))

