"""radar intercept"""
def main():
    """radius"""
    px1 = float(input())
    py1 = float(input())
    ce1 = float(input())
    px2 = float(input())
    py2 = float(input())
    ce2 = float(input())
    max_r = ce1 + ce2
    ranges = ((px1 - px2)**2+(py1-py2)**2)**0.5
    if max_r >= ranges:
        print("Yes")
    else:
        print("No")
main()
