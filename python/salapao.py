"""def main"""
def main():
    """def main"""
    midx = float(input())
    midy = float(input())
    rad = float(input())
    dotx = float(input())
    doty = float(input())
    if rad <= ((midx - midy)**2 + (dotx - doty)**2)**1/2:
        print("Yess!")
    else:
        print("Noo!")
main()
