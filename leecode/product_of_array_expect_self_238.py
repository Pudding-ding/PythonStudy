""""
# 238. 除自身以外数组的乘积
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
"""""

# 拆解为该元素左侧所有元素的乘积乘以右侧所有元素的乘积
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    # 先计算左乘积
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
    # 再从右往左乘上右乘积
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer

if __name__ == "__main__":
    nums = list(map(int, input("请输入数组（空格分隔）：").split()))
    print("方法一（左右数组）：", product_except_self(nums))

