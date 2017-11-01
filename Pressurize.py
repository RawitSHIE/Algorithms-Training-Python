"""
date : 21/09/2560
pair pro: Rawit & Supakit
judge : intersteller
"""
def main(inside, outside):
    """pressure"""
    if abs(inside-outside)*100/inside <= 30:
        print("Safe %.4f" %(abs(inside-outside)/inside*100)+"%")
    elif (inside-outside)/inside*100 > 0:
        print("Underpressure %.4f" %(abs(inside-outside)*100/inside)+"%")
    elif (inside-outside)/inside*100 < 0:
        print("Overpressure %.4f" %(abs(inside-outside)*100/inside)+"%")
main(float(input()), float(input()))
