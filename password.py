"""Password"""
def main():
    """change it"""
    import hashlib
    text = input()
    encode = hashlib.sha512(text.encode('utf-8')).hexdigest()
    print(encode.upper())
main()
