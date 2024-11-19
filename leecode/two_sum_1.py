""""
# 1.两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
"""""

# 法一：嵌套循环，遍历数组中的每两个数的和
def twosum1(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# 法二：利用字典两次遍历确定一个数找差值
def twosum2(nums, target):
    dict = {}
    # 遍历确定目标差值
    for i in range(len(nums)):
        dict[target - nums[i]] = i
    # 遍历找差值
    for i in range(len(nums)):
        if nums[i] in dict and dict[nums[i]] != i:
            return [i, dict[nums[i]]]
    return None

# 法三：利用哈希表--类似字典，与法二类似但一次遍历
def twosum3(nums, target):
    hashmap = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return None

# 检查
# 法一：与解法一相似，再确认一遍，为了方便调用，定义为新函数
def check1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

# 法二：利用集合遍历数组，与解法二类似，寻找差值，由于不需要输出索引，因此采用集合确定是否符合要求即可
def check2(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False

if __name__ == '__main__':
    nums = input('请输入整数数组如[2, 7, 11, 15]：')
    target = input('请输入任意目标值：')
    #检测输入值是否合理
    if not check1(nums, target):
    # if not check1(nums, target):
        print('输入数组与目标值不匹配，请重新开始！')
    else:
        result = twosum1(nums, target)
        # result = twosum2(nums, target)
        # result = twosum2(nums, target)