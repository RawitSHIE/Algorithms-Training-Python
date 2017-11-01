"""
pair programming
HorizontalHistogram
rawit 60070081
"""
def main():
    """hia"""
    alpha = {}
    for i in input():
        if i.isalpha() and i not in alpha:
            alpha[i] = 1
        elif i.isalpha():
            alpha[i] += 1
    for i in sorted(alpha):
        if i.islower():
            print(i, ("-----|"*(alpha[i]//5) + "-----|"[:alpha[i]%5]).rstrip("|"), sep=" : ")
    for i in sorted(alpha):
        if i.isupper():
            print(i, ("-----|"*(alpha[i]//5) + "-----|"[:alpha[i]%5]).rstrip("|"), sep=" : ")
main()
