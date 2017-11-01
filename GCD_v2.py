"""
pair programming
countletter
rawit 60070081
"""
def main():
    """ucide"""
    num1, num2 = int(input()), int(input())
    GCD = 0
    op_1 = min(num1, num2)
    op_2 = max(num1, num2)
    if num2 == 0 or num1 == 0:
        print(op_2)
    else:
        modu = op_2 % op_1
        for i in range(1, modu+1):
            if op_1 % i == 0 and modu % i == 0:
                GCD = i
    print(GCD)
main()
