""""
# 42.接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
# 计算按此排列的柱子，下雨之后能接多少雨水。
"""""
# 法一：一层一层的计算每层能装雨水的体积--时间复杂度 O(n × max_height)，超时了
def trap1(height):
    if not height:
        return 0
    total_water = 0
    max_height = max(height)
    n = len(height)

    for h in range(1, max_height + 1):
        left = 0
        right = n - 1
        # 左边指针移动到第一个大于等于当前层高的柱子
        while left < n and height[left] < h:
            left += 1
        # 右边指针移动到最后一个大于等于当前层高的柱子
        while right >= 0 and height[right] < h:
            right -= 1
        # 如果这一层无水就跳过
        if left >= right:
            continue
        # 计算该层中间有多少不是水的柱子
        layer_blocks = 0
        for i in range(left, right + 1):
            if height[i] >= h:
                layer_blocks += 1
        # 该层的水量 = 总宽度 - 实心柱子
        total_water += (right - left + 1 - layer_blocks)
    return total_water

# 法二：逐行换成逐列，一次顺序遍历、一次逆序遍历，分别获得每一个空格的前后信息，再一次遍历计算雨水数
def trap2(height):
    if not height or len(height) < 3:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    # 从左往右构造左边最大值
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    # 从右往左构造右边最大值
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    # 遍历每个位置，水量 = min(左高, 右高) - 自身高度
    total_water = 0
    for i in range(n):
        water = min(left_max[i], right_max[i]) - height[i]
        total_water += max(water, 0)  # 防止负值
    return total_water


# 法三：双指针法：每个位置可能接的水是 min(left_max, right_max) - height[i]，用两个指针从两侧向中间收缩
def trap3(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]  # 更新左边最大值
            else:
                total_water += left_max - height[left]  # 当前位置能装的水
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]  # 更新右边最大值
            else:
                total_water += right_max - height[right]
            right -= 1
    return total_water


if __name__ == "__main__":
    raw = input("请输入柱子高度列表：")
    height = [int(x.strip()) for x in raw.split(',')]
    result = trap1(height)
    # result = trap2(height)
    # result = trap3(height)
    print(f"总共可以接的雨水量为：{result}")
