"""doc str"""
def main():
    """doc str"""
    num1 = (input())
    num2 = (input())
    num3 = (input())
    num4 = (input())
    gg1 = (max(num1, num2, num3))
    gg2 = (min(num1, num2, num3))
    gg3 = (num1+num2+num3) - gg1 - gg2
    if num4 > gg1:
        print(gg2, gg3, gg1, num4)
    elif num4 < gg2:
        print(num4, gg2, gg3, gg1)
    elif num4 < gg3:
        print(gg2, num4, gg3, gg1)
    else:
        print(gg2, gg3, num4, gg1)
main()
