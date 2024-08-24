def find(ms, ss):
    n = len(ms)
    m = len(ss)
    i = j = 0
    while i < n and j < m:
        if ms[i] == ss[j]:
            i += 1
            j += 1
        else:
            i += 1
            j = 0
    if j == m:
        return i - j
    else:
        return '-1'
if __name__ == '__main__':
    print(find(ms = 'asdfg',ss = 'sd'))
