"""Chess board"""
def main():
    """size"""
    height = int(input())
    width = int(input())
    print(" _"*width)
    print(("|"+ "_|"*width + "\n")*(height), end="")
main()
