""""
# 160. 相交链表
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""""
# 定义链表节点类
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 使用双指针法查找两个单链表的相交起始节点（或返回 None）。
def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    pA = headA
    pB = headB
    # 当 pA 和 pB 不相等时循环; 如果某个指针走到末尾，就切换到另一个链表的头部继续走
    # 这样两个指针走过的总长度相同，若有交点，就会在交点处相遇；否则在 None 处相等退出
    while pA is not pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA  # 或者 pB，都相等

if __name__ == "__main__":
    # 构造测试链表 A 和 B（
    # A = 1 → 2 → 3 → 4 → 5
    # B = 9 → 3 → 4 → 5  （从节点“3”起 intersection）
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    b1 = ListNode(9)
    b1.next = a3  # 交点在 a3

    headA = a1
    headB = b1
    inter = get_intersection_node(headA, headB)
    if inter:
        print("交点节点的值是：", inter.val)
    else:
        print("没有交点")
