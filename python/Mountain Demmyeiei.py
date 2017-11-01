"""Mountain Demmyeiei"""
def main():
    """ar rai mai ru"""
    raw = float(input())
    size = int(raw)
    for i in range(1, size*2, 2):
        for _ in range(size-1):
            print(("*"*i).center(size*2), end="")
        print(("*"*i).center(size*2))
main()
