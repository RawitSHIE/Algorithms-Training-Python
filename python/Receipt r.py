"""receipt"""
def main():
    """receipt"""
    price = float(input())
    vat = float(input())
    vatcon = price*vat
    ser = float(input())
    sercon = (price + vatcon)*ser
    print("Gross Total :", "%.2f" % price, "baht")
    print("VAT", "%.2f" % (vat*100) +"% :", "%.2f" % vatcon, "baht")
    print("Service Charge %.2f" %(ser*100) + "% :", "%.2f" % sercon, "baht")
    print("-"*30)
    print("Total :", "%.2f" %(price + vatcon + sercon), "baht")
main()
