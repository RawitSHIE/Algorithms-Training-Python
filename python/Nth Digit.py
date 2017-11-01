"""NTH DIGIT"""
def main():
    """NTH"""
    num = int(input())
    text = "123456789101112131415161718192021222324252627282930"
    if 0 < num < 52:
        print(text[num-1])
    else:
        print("Out of Range")
main()
