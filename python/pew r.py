"""weapon fire"""
def main():
    """auto / semi"""
    fire = str(input())
    if  (fire.count("pew")%2 == 0 and fire.count("pew") != 0) and fire.count("pew") < 6:
        print("Semi-Automatic")
    elif fire.count("pew") == 1:
        print("Semi-Automatic")
    elif fire.count("pew") >= 3:
        print("Automatic")
    else:
        print("Safe")
main()
