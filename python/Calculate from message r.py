"""codition message"""
def main():
    """condition"""
    texta = input()
    textb = input()
    if len(texta)%2 == 0 and len(textb)%2 == 0:
        print(max(len(texta)**2, len(textb)**2))
        print(min(len(texta)**2, len(textb)**2))
    elif len(texta)%2 == 1 and len(textb)%2 == 1:
        print(max(len(texta)**3, len(textb)**3))
        print(min(len(texta)**3, len(textb)**3))
    else:
        print(abs((len(texta)**4)-(len(textb)**4)))
main()
