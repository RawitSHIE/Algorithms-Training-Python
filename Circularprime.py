"""
circularPrime
60070081
"""
def main():
    """ratio"""
    num = int(input())
    for i in range(2, num+1):
        for j in range(2, int(i**0.5) + 1):
            if i%j == 0 and i != 2:
                break
        else:
            seq =  [j for j in str(i)]
            print(seq)
main()


