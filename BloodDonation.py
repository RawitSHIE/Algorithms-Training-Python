"""
badblood
60070081
"""
def main():
    """tylor pls"""
    agree = "True"
    age = int(input())
    weight = int(input())
    attp = int(input())


    if age == 17 or 60 <= age <= 70:
        agree = input()
    if agree == "True":
        agree = True
    else:
        agree = False

    inrange = 17 <= age <= 70
    inweight = weight >= 45
    inattp = age < 55 or attp != 0

    if inrange and inweight and inattp and agree:
        print("Yes")
    else:
        print("No")
main()
