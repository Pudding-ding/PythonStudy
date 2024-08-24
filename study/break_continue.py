if __name__ == '__main__':
    #break

    for i in range(10):
        print(i)
        if i % 2 == 0:
            break
    #   if i % 2 ! == 0:余数
    #       break

    #continue
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
