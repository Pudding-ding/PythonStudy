print('这是pytestt会显示的内容')
def test():
    print('哈哈哈')
if __name__ == '__main__':#模块名被当作模块导入时，下面的代码不会被显示出来
    print('这是pytestt')
print('这是pytestt不会显示的内容')