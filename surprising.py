"""
    pair programming : surprising
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main():
    """rating"""
    total = float(input())
    highest = float(input())
    if total < highest*2:
        if highest > 2:
            print("Surprising")
        else:
            print("Not surprising")
    elif highest - (total - highest*2) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
