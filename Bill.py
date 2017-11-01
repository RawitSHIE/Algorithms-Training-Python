"""
judge : bill
pair : Rawit & Aof
date: 7/10/2560
"""
def main():
    """vatttt"""
    price = int(input())
    vat = price*0.10
    if 50 > vat:
        vat = 50
    elif vat > 1000:
        vat = 1000
    total = (vat + price)*1.07
    print("%.2f" %total)
main()
