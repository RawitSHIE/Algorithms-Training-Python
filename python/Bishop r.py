"""bishop"""
def main():
    """chess """
    pos1 = input()
    hor1 = pos1[0].upper()
    ver1 = pos1[1]
    pos2 = input()
    hor2 = pos2[0].upper()
    ver2 = pos2[1]
    if abs(int(ord(hor1))-int(ord(hor2))) == abs(int(ver1) - int(ver2)):
        print("True")
    else:
        print("False")
main()
