"""
safe
60070081
"""
def main():
    """shifed"""
    origin = input()
    encode = input()

    shift = 0
    for i in range(len(origin)):
        direct = abs(ind(origin[i]) - ind(encode[i]))
        invers = abs(26 - direct)
        shift += min(direct, invers)
    print(shift)

def ind(alph):
    """index"""
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(alph)
main()
