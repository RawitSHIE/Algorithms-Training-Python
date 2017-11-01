"""def main"""
def main():
    """doc str"""
    hor = int(input())
    mnu = int(input())
    mth = (input()).upper()
    if mth == "AM" and hor == 12 and mnu == 0:
        print("24 Hours time is", "%02d" %(hor-12), ":", "%02d" %mnu)
    elif mth == "AM":
        print("24 Hours time is", "%02d" %hor, ":", "%02d" %mnu)
    elif mth == "PM" and hor == 12:
        print("24 Hours time is", "%02d" %hor, ":", "%02d" %mnu)
    elif mth == "PM":
        print("24 Hours time is", "%02d" %(hor+12), ":", "%02d" %mnu)
main()
