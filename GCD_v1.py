"""
pair programming : 12/10/17
judge: GCD_v1
"""
def main():
    """find highest factor of both"""
    num1 = int(input())
    num2 = int(input())
    listed = []
    for i in range(1, max(num1, num2)+1):
        if num2%i == 0 and num1%i == 0:
            listed.append(i)
    print(max(listed))
main()
