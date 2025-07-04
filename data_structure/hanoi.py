# 递归实例：汉诺塔
# n个盘子时：
# 1.把n-1个圆盘从A经过C移动到B
# 2.把第n个圆盘从A移动到C
# 3.把n-1个小圆盘从B经过A移动到C
# h(x)=2h(x-1)+1

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a ,c))
        hanoi(n-1, b, a, c)

hanoi(3, 'A', 'B', 'C')

