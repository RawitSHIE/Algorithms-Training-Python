"""Greedy"""
def main(money, count):
    """This is function main"""
    while 1:
        if money == 0:
            break
        if money >= 25:
            count += money//25
            money = money-(money//25)*25
        elif 10 <= money < 25:
            count += money//10
            money = money-(money//10)*10
        elif 5 <= money < 10:
            count += money//5
            money = money-(money//5)*5
        else:
            count += money
            money = 0
    print(count)
main(int(input()), 0)