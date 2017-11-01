"""
    pair programming : Leap year
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main(year):
    """leap year"""
    if year%4 != 0:
        print("No")
    elif year%4 == 0 and year%100 != 0:
        print("Yes")
    elif year%100 == 0 and year%400 != 0 and year%4 == 0:
        print("No")
    elif year%4 == 0 or year%400 == 0:
        print("Yes")
    else:
        print("No")
main(int(input()))
