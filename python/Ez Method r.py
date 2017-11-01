"""EZ Method"""
def main():
    """case check condition"""
    texta = input()
    textb = input()
    if texta.islower() and textb.islower():
        print(texta.upper())
        print(textb.upper())
    elif texta.isupper() and texta.isupper():
        print(texta.lower())
        print(textb.lower())
    else:
        print("Python is so Ez")
main()
