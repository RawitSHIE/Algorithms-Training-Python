"""
pair programming
countletter
rawit 60070081
"""
def main():
    """count"""
    text = input()
    memo_1 = text[:1]
    letter = 0
    for i in text:
        if memo_1 == i:
            letter += 1
        else:
            print(str(letter)+memo_1, end="")
            memo_1 = i
            letter = 1
    print(str(letter)+memo_1)
main()
