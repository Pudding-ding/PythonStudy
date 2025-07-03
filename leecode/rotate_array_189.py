""""
# 189. 轮转数组
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""""
# 法一：创建一个新数组，把原数组元素按照轮转后的位置填进去
def rotate_array1(nums, k):
    n = len(nums)
    k = k % n  # 防止k超过长度
    res = [0] * n
    for i in range(n):
        res[(i + k) % n] = nums[i]
    return res

# 法二：创建新数组拼接
def rotate_array2(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k]

# 法三：先反转整个数组，再反转前k个，再反转后面的
def rotate_array3(nums, k):
    n = len(nums)
    k = k % n
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    reverse(0, n - 1)      # 反转整个数组
    reverse(0, k - 1)      # 反转前 k 个
    reverse(k, n - 1)      # 反转后 n-k 个

if __name__ == "__main__":
    nums = list(map(int, input("请输入数组（空格分隔）：").split()))
    k = int(input("请输入轮转步数 k："))
    print(rotate_array1(nums[:], k))
    # print(rotate_array2(nums[:], k))

    # #法三
    # nums_copy = nums[:]
    # rotate_array3(nums, k)
    # print(nums_copy)
