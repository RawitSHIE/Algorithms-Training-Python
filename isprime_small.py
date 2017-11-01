"""
pair programming : 12/10/17
judge: isprime
"""
def main():
    """is prime"""
    num = int(input())
    point = 0
    for i in range(1, num+1):
        if num%i == 0:
            point += 1
    if point == 2:
        print("Yes")
    else:
        print("No")
main()
