"""
Parallelogram
60070081
"""
def main():
    """eatsome pz"""
    text = input()
    leng = len(text)
    for i in range(leng):
        print(" "*(len(text)-(i+1)) + text[:i+1])
    for i in range(1, leng):
        print(text[i:])
main()
