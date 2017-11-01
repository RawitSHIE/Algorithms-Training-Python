"""doc str"""
def main():
    """doc str"""
    txt = input()
    if txt[-1:].isdigit():
        print((str(txt[-1:])+str(txt)+"\n")*15, end='')
    elif len(txt) == 1 and txt.isdigit():
        print((str(txt[-1:])+str(txt)+"\n")*15, end='')
    elif txt[:1] in "AEIOUaeiou":
        print((str(txt[::-1])+"\n")*69, end='')
    else:
        print((txt + "\n")*96, end='')
main()
