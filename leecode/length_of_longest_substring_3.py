""""
# 3.无重复字符的最长子串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
"""""
# 法一：用字符串存储当前子串。当前字符不在字串时，加入；存在时，一直删左边。
def length_of_longest_substring1(s):
    sub_str = ""  # 当前窗口的无重复子串
    max_len = 0
    for ch in s:
        if ch in sub_str:
            idx = sub_str.index(ch) # 删除从左到重复字符的位置
            sub_str = sub_str[idx + 1:]
        sub_str += ch  # 将当前字符加入子串
        max_len = max(max_len, len(sub_str))  # 更新最大长度
    return max_len

# 法二：用两个指针框住一个不重复的区间利用集合快速判断字符是否重复
def length_of_longest_substring2(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])   # 出现重复字符，左指针右移并移除
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

# 法三：与法二类似但利用字典
def length_of_longest_substring3(s):
    char_dict = {}  # 用于记录字符上次出现的位置
    max_len = 0
    left = 0
    for right in range(len(s)):
        ch = s[right]
        if ch in char_dict and char_dict[ch] >= left:    # 如果当前字符出现过，且在范围内左边界右移
            left = char_dict[ch] + 1
        char_dict[ch] = right  # 更新字符的最新位置
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s = input("请输入一个字符串：")
    result = length_of_longest_substring1(s)
    # result = length_of_longest_substring2(s)
    # result = length_of_longest_substring3(s)
    print("最长不重复子串长度为：", result)
