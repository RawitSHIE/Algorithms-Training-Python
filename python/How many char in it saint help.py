"""How many char in it"""
TEXT_1 = list(input())
def cout(val):
    """Because we can use count()"""
    num = 0
    for j in range(sum(1 for x in TEXT_1)):
        if val == TEXT_1[j]:
            num += 1
    return num

def main():
    """chr count"""
    lower, upper, nlow, nup = [], [], [], []
    text2 = sorted(set(TEXT_1))
    for che in TEXT_1:
        if che.isalpha() == True:
            has_alpha = True
            break
        else:
            has_alpha = False
    if has_alpha == False:
        print("\\@#!$#\'\\\\\"$!%&{\"")
    while has_alpha:
        for j in range(sum(1 for x in text2)):
            if text2[j] in 'abcdefghijklmnopqrstuvwxyz':
                lower.append(text2[j])
                nlow.append(cout(text2[j]))
            elif text2[j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                upper.append(text2[j])
                nup.append(cout(text2[j]))
        lista = lower + upper
        listb = nlow + nup
        for k in range(sum(1 for x in lista)):
            print(lista[k], ":", listb[k])
        break
main()
