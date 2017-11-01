"""How many char in it"""
def main():
    """chr count"""
    text = list(input())
    lower, upper, nlow, nup = [], [], [], []
    alpha = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(len(alpha)):
        if alpha[i] in text:
            text2 = sorted(set(text))
            for j in range(len(text2)):
                if text2[j] in 'abcdefghijklmnopqrstuvwxyz':
                    lower.append(text2[j])
                    nlow.append(text.count(text2[j]))
                elif text2[j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    upper.append(text2[j])
                    nup.append(text.count(text2[j]))
            lista = lower + upper
            listb = nlow + nup
            for k in range(len(lista)):
                print(lista[k],":" , listb[k])
            break
        elif not(alpha[len(alpha)-1] in text):
            print("\\@#!$#'\\\\\"$!%&{\"")
            break
main()
