"""
60070081
BookWorm
"""
def worm():
    """without books I won't be here"""
    book = []
    for i in range(int(input())):
        mnu = int(input())
        left = int(input())
        total = sorted([int(input()) for _ in range(left)])
        tmp = 0
        count = 0
        for j in total:
            if j + tmp <= mnu:
                tmp += j
                count += 1
            else:
                break
        book += [count]

    for i in book:
        print(i)

worm()
