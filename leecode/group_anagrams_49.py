""""
# 49.字母异位词
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
"""""


# 法一：对每一个字符串进行其跟其他没有分组的字符串是否为异位词。是就判为一组
def is_anagram(a, b):
    return sorted(a) == sorted(b)

def group_anagrams1(strs):
    res = []                     # 最终结果
    used = [False] * len(strs)   # 标记哪些字符串已经被分组
    for i in range(len(strs)):
        if used[i]:
            continue
        group = [strs[i]]   # 新建一个组，包含当前字符串
        used[i] = True      # 标记该字符串已被使用
        for j in range(i+1, len(strs)):
            # 如果没用过，并且与当前字符串是异位词
            if not used[j] and is_anagram(strs[i], strs[j]):
                group.append(strs[j])  # 加入当前组
                used[j] = True         # 标记为已使用
        res.append(group)
    return res

# 法二：对每个字符串进行字母排序，排序后的结果作为 key，存到字典中。异位词排序后相同
def group_anagrams2(strs):
    dict = {}
    for word in strs:
        # 将字符串排序后作为key
        key = ''.join(sorted(word))
        if key not in dict:  # 如果这个key不存在就先初始化
            dict[key] = []
        # 将原始字符串加入对应的分组
        dict[key].append(word)
    return list(dict.values())

# 法三：记录26个字母每个出现的个数，将结果作为key保存在字典当中。
from collections import defaultdict
def group_anagrams3(strs):
    dict = defaultdict(list)  # defaultdict(list)自动初始化列表的字典，避免手动初始化报错

    for word in strs:
        count = [0] * 26  # 统计每个字母出现次数，a~z 对应到 0~25方便索引确定
        for c in word:
            # 将字符转换为对应位置索引，并加一
            count[ord(c) - ord('a')] += 1  # ord(char)是为了返回某个字符的ASCLL编码
        key = tuple(count)  # 将列表转换为元组而不是list是为了保持顺序不变
        dict[key].append(word)
    return list(dict.values())

if __name__ == '__main__':
    strs = eval(input("请输入字符串数组，例如 ['eat','tea','tan','ate','nat','bat']："))
    result = group_anagrams1(strs)
    # result = group_anagrams2(strs)
    # result = group_anagrams3(strs)
    print("分组结果如下：")
    print(result)
