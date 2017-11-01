"""direction"""
def main():
    """Navigation degree"""
    com = str(input()).upper()
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    degree = num1 + num2 + num3 + num4
    rdegree = degree%360
    deg = int(rdegree/90)
    if degree % 90 == 0:
        if  com == "N":
            din = "NESW"
            print(din[deg])
        elif    com == "E":
            die = "ESWN"
            print(die[deg])
        elif    com == "S":
            dis = "SWNE"
            print(dis[deg])
        elif    com == "W":
            diw = "WNES"
            print(diw[deg])
    else:
        print("Error")
main()
