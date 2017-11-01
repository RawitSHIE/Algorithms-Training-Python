"""Final fantasy"""
def main(dama, boss, size, skill):
    """toggle"""
    print("o--------------------o")
    dama7 = "%07d" %dama
    print("|"+"%-20s" %dama7+"|")
    if size%2 == 0:
        size = size
    else:
        size += 1
    bosao = boss*size
    print("|"+bosao.center(20)+"|")
    print("|"+bosao.center(20)+"|")
    print("|"+bosao.center(20)+"|")
    print("|____________________|")
    if skill == 1:
        print("| "+">"+"Tackle", " "+"Iron tail"+" |")
        print("| "+" "+"Growl ", " "+"Flash    "+" |")
    elif skill == 2:
        print("| "+" "+"Tackle", ">"+"Iron tail"+" |")
        print("| "+" "+"Growl ", " "+"Flash    "+" |")
    elif skill == 3:
        print("| "+" "+"Tackle", " "+"Iron tail"+" |")
        print("| "+">"+"Growl ", " "+"Flash    "+" |")
    elif skill == 4:
        print("| "+" "+"Tackle", " "+"Iron tail"+" |")
        print("| "+" "+"Growl ", ">"+"Flash    "+" |")
    print("o--------------------o")
main(int(input()), input(), int(input()), int(input()))
