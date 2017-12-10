"""
pair programming
Diamond1
60070108
60070081
"""
def main():
    """the chick"""
    depth = int(input())
    num = int(input())
    summ = list()
    for _ in range(depth):
        chick = input().split()
        chick = [int(x) for x in chick]
        for j in range(num):
            summ.append(0)
            summ[j] += chick[j]
    print(max(summ))
main()