""""
11.盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
"""""
# 法一：两次循环嵌套算出每两个的盛水量（面积），比较出最大的量
def max_water1(height):
    max_water = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1, n):
            h = min(height[i], height[j])       # 取左右两边中较小的高度
            w = j - i                           # 两指针的距离是计算面积的宽度
            max_water = max(max_water, h * w)   # 计算当前容量，取最大值
    return max_water

# 法二：使用双指针法计算，左右各一指针，每次移动短板以尝试增大容量
# 双指针类似与夹逼思想吧，对于数组中的每个数据只遍历一次，两端都在逼近最优结果。
def max_water2(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)
        # 移动短指针限制容积
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

if __name__ == "__main__":
    raw = input("请输入高度数组,例如 1,8,6,2,5,4,8,3,7：")
    height = [int(x.strip()) for x in raw.split(',') if x.strip().lstrip('-').isdigit()]
    result = max_water1(height)
    # result = max_water2(height)
    print("最大可盛水量为：", result)
