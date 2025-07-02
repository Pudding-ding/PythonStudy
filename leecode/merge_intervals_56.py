""""
# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，
# 其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，
# 并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""""

# 先按照区间起始位置排序，然后遍历每个区间，如果当前区间和上一个合并后的区间有重叠，就合并
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])  # 按起始位置排序
    merged = [intervals[0]]  # 初始化结果集
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # 有重叠
            last[1] = max(last[1], current[1])  # 合并
        else:
            merged.append(current)  # 无重叠，直接加入
    return merged

if __name__ == "__main__":
    raw = input("请输入区间数组（如 1 3, 2 6, 8 10）：")
    # 把输入字符串转为区间列表
    intervals = [list(map(int, pair.split())) for pair in raw.split(',')]
    print("合并后的区间为：", merge_intervals(intervals))
