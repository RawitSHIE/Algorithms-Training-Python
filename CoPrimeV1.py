"""
pair programming : 12/10/17
judge: Co_primeV1
"""
def main():
    """find highest factor of both"""
    num1 = int(input())
    num2 = int(input())
    listed = []
    for i in range(1, max(num1, num2)+1):
        if num2%i == 0 and num1%i == 0:
            listed.append(i)
    if max(listed) == 1:
        print("YES")
    else:
        print("NO")
    print(max(listed))
main()
