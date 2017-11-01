"""
    pair programming : Inflation
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main():
    """count year max rate"""
    amount = int(float(input())*100)
    print(amount)
    years = int(input())
    for _ in range(years):
        amount = (amount*10381)//10000
        print(amount)
    print('%d.%02d' % (amount//100, amount%100))
main()
