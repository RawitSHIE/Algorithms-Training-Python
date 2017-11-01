"""a^n (rerun)"""
def main():
    """exponent"""
    base = int(input())
    expo = int(input())
    expo2 = 0
    expo3 = 0
    if expo != 0:
        for _ in range(expo):
            for _ in range(base):
                base += base
        print(expo2)
    else:
        print(0)
main()
