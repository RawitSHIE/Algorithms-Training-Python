"""
60070081
OneComplement
"""
def main():
    """they wanna kill me"""
    mac = ""
    space = int(input())
    get = input()
    num = int(get)
    if get == "-0":
        print("1"*space)
    else:
        tmp = int(num)
        if num > 0:
            while tmp != 0:
                mac += str(tmp%2)
                tmp = tmp//2
        elif num < 0:
            while abs(tmp) != 0:
                if abs(tmp) % 2 == 0:
                    mac += "1"
                else:
                    mac += "0"
                tmp = abs(tmp)//2
        if space == 0:
            pass
        elif num < 0:
            print(("1"*(max(0, space-len(mac))) + mac[::-1])[-space:])
        else:
            print(("0"*(max(0, space-len(mac))) + mac[::-1])[-space:])
main()
