"""length"""
def main():
    """str length"""
    text_le = len(input())
    if text_le <= 3:
        print("Yes")
    elif 4 <= text_le <= 10:
        print("No")
    elif 11 <= text_le <= 20:
        print("Ok")
    elif text_le <= 100:
        print("Thank You")
    else:
        print("OMFG To Many For Me GG")
main()
