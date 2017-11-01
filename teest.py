"""test donut"""
def main():
    """dont agian"""
    price = int(input())
    amount = int(input())
    free = int(input())
    demand = int(input())

    set_value = demand//(amount+free)
    left_value = demand%(amount+free)

    if left_value > amount:
        get = set_value*(amount+free+1)
        paid = price*(set_value+1)*amount

    else:
        get = set_value*(amount+free) + left_value
        paid = price*((set_value)*amount + left_value)

    print(paid, get)
main()
