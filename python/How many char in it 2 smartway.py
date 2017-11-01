"""How many char in it?? V.1"""
def how_many():
    """How many char in it?? V.1"""
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = input()
    chk = 1
    for i in alpha:
        if i in text:
            print(i, ":", nub(text, i))
            chk = 0
    if chk:
        print("\\@#!$#'\\\\\"$!%&{\"")
def nub(text=str(), chk=str()):
    """nubtuasum"""
    num = 0
    for i in text:
        if i == chk:
            num += 1
    return num
how_many()
