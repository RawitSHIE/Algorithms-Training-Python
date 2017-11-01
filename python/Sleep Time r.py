"""sleep time"""
def main():
    """convert"""
    slepthor = int(input())
    sleptmnu = int(input())
    wakehor = int(input())
    wakemnu = int(input())
    if slepthor > wakehor and sleptmnu > wakemnu:
        hor = ((24 - slepthor) + wakehor) - 1
        mnu = (60 - sleptmnu) - wakemnu
        print(hor, "%02d" %mnu, sep=":")
    elif slepthor > wakehor and sleptmnu < wakemnu:
        hor = ((24 - slepthor) + wakehor)
        mnu = wakemnu - sleptmnu
        print(hor, "%02d" %mnu, sep=":")
    elif slepthor > wakehor and sleptmnu == wakemnu:
        hor = ((24 - slepthor) + wakehor)
        print(hor, "00", sep=":")
    elif slepthor < wakehor and sleptmnu > wakemnu:
        hor = wakehor - slepthor -1
        mnu = (60 - sleptmnu) - wakemnu
        print(hor, "%02d" %mnu, sep=":")
    elif slepthor < wakehor and sleptmnu < wakemnu:
        hor = wakehor - slepthor
        mnu = wakemnu - sleptmnu
        print(hor, "%02d" %mnu, sep=":")
    elif slepthor < wakehor and sleptmnu == wakemnu:
        hor = wakehor - slepthor
        print(hor, "00", sep=":")
    elif slepthor == wakehor and sleptmnu < wakemnu:
        mnu = wakemnu - sleptmnu
        print("0", "%02d" %mnu, sep=":")
    elif slepthor == wakehor and sleptmnu > wakemnu:
        mnu = (60 - sleptmnu) - wakemnu
        print("23", "%02d" %mnu, sep=":")
main()
