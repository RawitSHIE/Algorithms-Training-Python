"""
date : 21/09/2560
pair pro: Rawit & Supakit
judge : SecondConverter
"""
def main():
    """time converter"""
    tal = int(input())
    sec_min = int(input())
    min_hour = int(input())
    hour_day = int(input())
    real_sec = tal%sec_min
    real_min = tal//sec_min
    real_hour = real_min//min_hour % hour_day
    print(real_hour, real_min%min_hour, real_sec, sep=":")
main()
