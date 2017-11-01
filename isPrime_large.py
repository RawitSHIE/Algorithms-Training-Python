"""
pair programming
isPrime_large
rawit 60070081
"""
def main():
    """sq num"""
    numfind = int(input())
    if numfind == 2:
        print("YES")
    elif numfind == 1:
        print("NO")
    else:
        for i in range(2, int(numfind**0.5)+1):
            if numfind%i == 0:
                print("NO")
                break
        else:
            print("YES")
main()
