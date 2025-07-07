""""
# 48.旋转图像
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""""

def rotate(matrix):
    n = len(matrix)
    # 先转置
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #再反转
    for row in matrix:
        row.reverse()

    # 或者利用内置函数两行搞定
    # matrix[:] = list(map(list, zip(*matrix)))
    # for row in matrix: row.reverse()

if __name__ == "__main__":
    print("请输入 n × n 矩阵（每行以空格分隔，输入空行结束）：")
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        matrix.append(list(map(int, line.strip().split())))

    rotate(matrix)
    print("旋转后的矩阵为：")
    for row in matrix:
        print(row)
