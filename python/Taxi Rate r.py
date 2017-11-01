"""TAXI"""
import math
def main():
    """TAXI METER"""
    kilo = int(input())
    sec = int(input())
    price = 0
    if 0 <= kilo:
        price += 50
    if 2 <= kilo:
        price += min((kilo-1) * 5, 45)
    if 11 <= kilo:
        price += min((kilo-10) * 7.5, 75)
    if 21 <= kilo:
        price += min((kilo-20) * 10, 200)
    if 41 <= kilo:
        price += min((kilo-40) * 12.5, 312.5)
    if 65 < kilo:
        price += (kilo-65) * 15
    price += math.ceil(sec/60) * 1.5
    print(math.ceil(price))
main()
