"""""
283.移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""""

# 法一：交换次序，慢慢移动到末尾
def move_zeroes1(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] == 0 and nums[j + 1] != 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# 法二：把数一个个提取出来，非零的放在最前面，零放最后面
def move_zeroes2(nums):
    insert = 0
    for num in nums:
        if num != 0:
            nums[insert] = num
            insert += 1
    # 将剩下的位置填 0
    for i in range(insert_, len(nums)):
        nums[i] = 0

# 示例用法
if __name__ == "__main__":
    raw = input("请输入数组（用英文逗号分隔，例如 0,1,0,3,12：")
    nums = [int(x.strip()) for x in raw.split(',') if x.strip().lstrip('-').isdigit()]

    print("原数组：", nums)
    move_zeroes1(nums)
    # move_zeroes2nums)
    print("移动后：", nums)
