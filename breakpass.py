"""decryptPassword"""
def main():
    """hash"""
    import hashlib
    text = input()
    for i in range(100000):
        tmp = "%05d" %i
        encode2 = hashlib.sha512(tmp.encode('utf-8')).hexdigest()
        if encode2 == text.lower():
            print(tmp)
            break
main()
