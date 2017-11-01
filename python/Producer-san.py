"""doc str"""
def main():
    """doc str"""
    name = input()
    age = int(input())
    sle = input()
    if len(name)*1.5 > 9:
        names = 10
    else:
        names = len(name)*1.5
    if (30 - age)*0.5 >= 10:
        ages = 10
    elif age > 30:
        ages = 0
    else:
        ages = (30 - age)*0.5
    if sle == "Egao":
        sles = 10
    elif sle == "Yes":
        sles = 5
    elif sle == "No":
        sles = 0
    else:
        sles = len(sle)*-0.5
    print("Name :", name)
    print("Score : %.1f" %max(names + sles + ages, 0))
    if (names + sles + ages) >= 15:
        print("Pass Project Cinderella")
    else:
        print("Not Pass")
main()
