"""
pair programming
SqFree
rawit 60070081
"""
def main():
    """sq free"""
    num = int(input())
    count = 1
    for j in range(2, num):
        for i in range(2, j+1):
            if i**2 > j or j%(i**2) == 0:
                break
            elif j%(i**2) != 0:
                count += 1
                break
    print(count)
main()

