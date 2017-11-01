"""
pair programming : 12/10/17
judge: Binary
"""
def main():
    """mod and ignore"""
    num = int(input())
    listed = []
    while 1:
        listed.append(str(num%2))
        num = num//2
        if not num:
            break
    print("".join(listed[::-1]))
main()
