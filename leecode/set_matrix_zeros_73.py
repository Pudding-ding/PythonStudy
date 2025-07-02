""""
# 73.矩阵置0
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。
# 请使用 原地 算法。
"""""
# 法一：记录每行每列，若有0整行整列置0，注意要先确定是哪行哪列再统一置0
def set_zeroes1(matrix):
    m, n = len(matrix), len(matrix[0])
    row_zero = set()
    col_zero = set()
    for i in range(m):    # 先遍历找出0的位置
        for j in range(n):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)
    for i in range(m):    # 同行同列变为0
        for j in range(n):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0

# 法二：使用 第一行和第一列 作为标记位，记录哪些行和列需要置 0。
def set_zeroes2(matrix):
    m, n = len(matrix), len(matrix[0])
    row0 = any(matrix[0][j] == 0 for j in range(n))  # 第一行是否需要清零
    col0 = any(matrix[i][0] == 0 for i in range(m))  # 第一列是否需要清零
    for i in range(1, m):    # 使用第一行第一列作为标记位
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):    # 根据标记位清零
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if row0:    # 处理第一行
        for j in range(n):
            matrix[0][j] = 0
    if col0:    # 处理第一列
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    print("请输入矩阵，空格分隔，行回车，结束请输入空行")
    matrix = []
    while True:
        row = input()
        if not row:
            break
        matrix.append(list(map(int, row.strip().split())))
    set_zeroes1(matrix)
    # set_zeroes2(matrix)
    print("置零后的矩阵：")
    for row in matrix:
        print(row)

