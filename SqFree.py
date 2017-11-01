"""
pair programming
SqFree
rawit 60070081
"""
def main():
    num = int(input())
    count = 0
    for j in range(2, num):
        for i in range(2, j+1):
            if i**2 > j:
                break
            elif j%(i**2) == 0:
                count += 1
    print(count)
main()


