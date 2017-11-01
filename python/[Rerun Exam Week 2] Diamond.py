"""diamond"""
def main():
    """rint for"""
    size = int(input())
    for i in range(1, size*2, 2):
        print(("*"*i).center(size*2))
    for j in range(3, size*2, 2):
        print(("*"*(size*2-j)).center(size*2))
main()
