""""
# 54.螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""""
def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    res = []
    m, n = len(matrix), len(matrix[0])
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        # 从左到右
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        # 从上到下
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        # 从右到左（必须再次判断）
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        # 从下到上
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res

if __name__ == "__main__":
    print("请输入矩阵（每行以空格分隔，输入空行结束）：")
    matrix = []
    while True:
        row = input()
        if not row.strip():
            break
        matrix.append(list(map(int, row.strip().split())))

    result = spiral_matrix(matrix)
    print("顺时针螺旋遍历结果：", result)
