"""
    pair programming : Circular2
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main():
    """radius"""
    per_x = float(input())
    per_y = float(input())
    per_r = float(input())
    mos_x = float(input())
    mos_y = float(input())
    mos_r = float(input())
    dis = ((per_x-mos_x)**2+(per_y-mos_y)**2)**0.5
    save = per_r + mos_r
    if dis >= save:
        print("No")
    else:
        print("Yes")
main()
