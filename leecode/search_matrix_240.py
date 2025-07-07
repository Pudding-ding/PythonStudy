""""
# 240. 搜索二维矩阵
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
"""""

# 法一：直接暴力查找
def search_matrix1(matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False

# 法二：从右上角开始类似二叉树寻找，同理也可尝试每行二分查找
def search_matrix2(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    print("请输入矩阵（每行以空格分隔，输入空行结束）：")
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        matrix.append(list(map(int, line.strip().split())))

    target = int(input("请输入目标值："))
    found = search_matrix1(matrix, target)
    # found = search_matrix2(matrix, target)
    print("查找结果：", found)

