"""
    pair programming : Leap year
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
    save = ((per_x-mos_x)**2+(per_y-mos_y)**2)**0.5
    if save > per_r:
        print("No")
    else:
        print("Yes")
main()
