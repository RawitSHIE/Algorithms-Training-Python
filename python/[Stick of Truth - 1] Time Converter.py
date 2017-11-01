"""[Stick of Truth - 1] Time Converter"""
def main():
    """convert"""
    hor_pal = int(input())*50*29
    mnu_pal = int(input())*29
    sec_pal = int(input())
    #converted -> real time
    time_real = (hor_pal + mnu_pal + sec_pal)*14
    #divide
    day_real = time_real//(3600*24)
    hor_real = (time_real - day_real*24*3600)//3600
    mnu_real = (time_real - (hor_real*3600 + day_real*24*3600))//60
    sec_real = time_real - (hor_real*3600 + mnu_real*60 + day_real*24*3600)
    print("%02d" %hor_real, "%02d" %mnu_real, "%02d" %sec_real, sep=":")
    print("Day :", day_real)
main()
