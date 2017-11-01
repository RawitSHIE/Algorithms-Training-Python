"""def main"""
def main():
    """defffffff"""
    number = int(input())
    primeset = []
    for i in range(2, number+1):
        isprime = True
        for j in range(3, i):
            if i%j == 0:
                isprime = False
                break
        if isprime:
            primeset.append(i)
    print(primeset)
    for i in primeset:
        for j in primeset:
            for k in primeset:
                if i + j + k == number:
                    print(i,j,k)
main()
