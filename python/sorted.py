"""doc str"""
def main():
    """doc str"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    gg1 = (max(num1, num2, num3))
    gg2 = (min(num1, num2, num3))
    gg3 = (num1+num2+num3) - gg1 - gg2
    if num4 > gg1:
        print(gg2)
        print(gg3)
        print(gg1)
        print(num4)
    elif num4 < gg2:
        print(num4)
        print(gg2)
        print(gg3)
        print(gg1)
    elif num4 < gg3:
        print(gg2)
        print(num4)
        print(gg3)
        print(gg1)
    else:
        print(gg2)
        print(gg3)
        print(num4)
        print(gg1)
main()
