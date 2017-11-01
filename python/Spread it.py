"""Spread it"""
def main():
    """range thx"""
    text = input()
    number = []
    text2 = "".join(text)
    text3 = sorted(set(list(text2)))
    for i in range(len(text3)):
        pos = text2.count(text3[i])
        number.append(pos)
    print(text3[::-1])
    print(number[::-1])
main()
