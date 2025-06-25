""""
# 428.找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
"""""

from collections import Counter

def find_anagrams(s, p):
    res = []
    len_p = len(p)
    counter_p = Counter(p)   # counter计数器，类似特殊的字典，统计元素及其出现的次数

    for i in range(len(s) - len_p + 1):
        ran = s[i:i + len_p]
        if Counter(ran) == counter_p:
            res.append(i)
    return res

if __name__ == "__main__":
    s = input("请输入主串 s：")
    p = input("请输入目标串 p：")
    print("所有异位词的起始索引为：", find_anagrams(s, p))