""""
# 15. 三数之和
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
"""""
# 法一：三层循环嵌套，利用集合去重，求出所有三个数相加为0的结果
def three_sum(nums):
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)
    return [list(t) for t in res]  #集合转化为列表

# 法二：同一类似，但先排序，并且利用集合寻找的是两数之和等于第一个数的相反数
def three_sum2(nums):
    nums.sort()   # 排序
    n = len(nums)
    res = set()
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的num[i]值
            continue
        seen = set()
        target = -nums[i]  # 目标是找到两数之和为-nums[i]
        for j in range(i + 1, n):
            complement = target - nums[j]
            if complement in seen:
                res.add((nums[i], complement, nums[j]))
            seen.add(nums[j])
    return [list(t) for t in res]

# 法三：双指针法，先对数组排序，法二延伸，先固定一个数，然后对剩余的数组使用左右指针找两个数，是的最终结果为0
def three_sum3(nums):
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的 nums[i]
            continue
        target = -nums[i] # 目标是找到两数之和为-nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # 跳过重复的 left 和 right
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 移动指针继续查找
                left += 1
                right -= 1
            elif total < target:
                left += 1  # 和太小，左指针右移
            else:
                right -= 1  # 和太大，右指针左移
    return res

if __name__ == "__main__":
    raw = input("请输入整数数组：")
    nums = [int(x.strip()) for x in raw.split(',')]

    print("所有和为0的三元组为：", three_sum1(nums))
    # print("所有和为0的三元组为：", three_sum2(nums))
    # print("所有和为0的三元组为：", three_sum3(nums))