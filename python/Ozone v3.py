"""Ozonev3"""
def main():
    """v33"""
    num = float(input())*100
    for i in range(1, int((num+1))):
        print(("* "*i).center(int((num)*2 - 1)))
    print(("* *").center(int((num)*2 - 1)))
    print(("* *").center(int((num)*2 - 1)))
    print(("*"*5).center(int((num)*2 - 1)))
main()
