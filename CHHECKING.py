"""
Sedthwuth Maisonti No.60070109
week8 15/10/2017
"""
def main(price, dounut, free, demand):
    """Dounut is yum yum"""
    box = (dounut+free)
    want_set = demand//box
    left_dounut = demand%box
    dounut_all = box
    if left_dounut >= dounut:
        total_price = price*((want_set*box)+dounut)
        dounut_total = ((box*want_set)+dounut+free)
    else:
        total_price = price*((want_set*box)+left_dounut)
        dounut_total = ((box*want_set)+left_dounut)
    print(str(total_price)+" "+str(dounut_total))
main(int(input()), int(input()), int(input()), int(input()))
