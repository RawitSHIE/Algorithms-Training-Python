"""primenumber"""
def main():
    """sour"""
    num = int(input())
    if num > 1:
       #INTERNET HELP FOR THIS LINE
        for i in range(2, num):
            if (num % i) == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
main()
