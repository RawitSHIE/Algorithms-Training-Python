"""cinema pricing"""
def main():
    """person x price"""
    date = str(input()).lower()
    pers = int(input())
    if date in "monday tuesday":
        print(pers * 120)
    elif date == "wednesday":
        print(pers * 80)
    elif date in "thursday friday saturday sunday":
        print(pers * 140)
main()
