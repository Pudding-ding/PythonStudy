    ## a!
    # def test(n):
    #     result = 1
    #     for item in range(1, n+1)
    #         result = result * item
    #     return result
def tt(n):
    if n == 1:
        return n
    return n * tt(n - 1)
print(tt(3))
