"""
pair programming
perfect
rawit 60070081
"""
def perfect(num, res):
    """time for perfect"""
    lst = [2**(i-1)*(2**i-1) for i in [2, 3, 5, 7, 13]]
    for i in lst:
        if i <= num:
            res += i
    print(res)
perfect(int(input()), 0)
