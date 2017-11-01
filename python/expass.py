"""doc str"""
def main():
    """doc str"""
    pas = input()
    alpha, digit = [], []
    time = 0
    dele = -1
    condi = 0
    if len(pas) < 6:
        print("try again")
        pas = input()
        if len(pas) < 6:
            print("process terminated")
        else:
            if pas.isalpha():
                condi += 30
                if pas.islower():
                    condi += 100
                elif pas.isupper():
                    condi += 85
                else:
                    condi += 175
            elif pas.isdigit():
                condi += 50
            else:
                condi += 75
            dele = pas.count(pas[0])
            if dele > 3:
                condi -= (dele-3)*15
            if len(pas) > 10:
                condi += (len(pas)-10)*10
            condi += ord(pas[len(pas)-1])
            print("Password :", "*"*len(pas))
            print("Security score :", condi)
            sec1 = 150 > condi
            sec2 = condi < 300
            sec3 = condi >= 300
            print("Security level :", "poor"*sec1 + "acceptable"*sec2 + "secure"*sec3)
main()
