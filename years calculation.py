"""
    pair programming : Inflation
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main():
    """count year max rate"""
    amount = int(float(input())*10000)
    years = int(input())
    if amount >= 0 and years >= 0:
        for _ in range(years):
            amount = amount*1.0381//1
        amount = amount//100
        num1 = amount//100
        num2 = amount%100
        print("%.d.%02d" %(num1, num2))
        #print("%.2f" %(amount))
main()
