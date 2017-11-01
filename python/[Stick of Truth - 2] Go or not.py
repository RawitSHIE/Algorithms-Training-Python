"""[Stick of Truth - 2] Go or not"""
def main():
    """ไม้เท้าแห่งสัจธรรม"""
    dis = int(input())//1200
    bread = int(input())*2
    water = int(input())
    wait = int(input())
    width = int(input())
    tat = (wait - dis) + bread + water
    print("#"*width)
    if tat > 0:
        if width%2 == 0 or width < 4:
            print("#"+("Go").center(width-2)+"#")
        else:
            print("#"+("Go").center(width-3)+" #")
    else:
        if width%2 == 0 or width < 8:
            print("#"+("Not Go").center(width-2)+"#")
        else:
            print("#"+("Not Go").center(width-3)+" #")
    print("#"*width)
main()
