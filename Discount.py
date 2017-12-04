"""
Discount
60070081
"""
def main():
    """get 5 free 1"""
    book = []
    while True:
        scan = input()
        if scan == "ENTER":
            break
        else:
            book += [int(scan)]
    free = len(book)//5
    ran = sorted(book)
    if len(ran) < 20:
        free = min(2, len(book)//6)
    print(sum(ran[free:]))
main()
