def valid_parentheses(str):
    if len(str) % 2 == 1:
        return False
    while '()' in str or '[]' in str or '{}' in str:
        str = str.replace('()', '')
        str = str.replace('[]', '')
        str = str.replace('{}', '')
    return str == ''
# def testValid_parentheses():
#      print(valid_parentheses('({)}'))
if __name__ == '__main__':
    s = input('请输入仅包含()或[]或{}的字符串：')
    print(valid_parentheses(str = s))
