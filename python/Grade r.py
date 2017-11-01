"""Grade calculator"""
def main():
    """score input"""
    score = int(input())
    if 100 >= score >= 80:
        print("4.0")
    elif 79 >= score >= 75:
        print("3.5")
    elif 74 >= score >= 70:
        print("3.0")
    elif 69 >= score >= 65:
        print("2.5")
    elif 64 >= score >= 60:
        print("2.0")
    elif 59 >= score >= 55:
        print("1.5")
    elif 54 >= score >= 50:
        print("1.0")
    elif 50 > score:
        print("0.0")
main()
