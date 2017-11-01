"""
pair programming
SqFree
rawit 60070081
"""
def main():
    """main function"""
    num = int(input())
    count = 0
    for i in range(1, num+1):
        if sqfree(i):
            count = count + 1
    print(count)
def sqfree(num):
    """sqfree"""
    for i in range(2, int(num**0.5)+1):
        if num%(i**2) == 0:
            return 0
    return 1
main()