# 矩阵乘法

# 法一：矩阵乘法定义
def matmul1(A, B):
    m = len(A)     # A行数
    n = len(A[0])  # A列数，也是B行数
    p = len(B[0])  # B列数
    result = [[0 for _ in range(p)] for _ in range(m)]  # 结果矩阵
    # 矩阵乘法定义
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

#法二：转置了更好算
def matmul2(A, B):
    result = []
    B_T = list(zip(*B))  # zip(*B)将B转置
    for row in A:
        result.append([sum(a * b for a, b in zip(row, col)) for col in B_T])
    return result


if __name__ == "__main__":
    # 输入矩阵尺寸
    m = int(input("请输入矩阵A的行数："))
    n = int(input("请输入矩阵A的列数（=矩阵B的行数）："))
    p = int(input("请输入矩阵B的列数："))

    # 输入矩阵 A
    print("请输入矩阵A的每一行（以空格分隔）：")
    A = []
    for _ in range(m):
        row = list(map(int, input().split()))
        A.append(row)

    # 输入矩阵 B
    print("请输入矩阵B的每一行（以空格分隔）：")
    B = []
    for _ in range(n):
        row = list(map(int, input().split()))
        B.append(row)

    # 输出结果
    print("\n法一结果：")
    for row in matmul1(A, B):
        print(row)

    print("\n法二结果：")
    for row in matmul2(A, B):
        print(row)
