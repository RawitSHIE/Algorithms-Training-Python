"""donut"""
def main():
    """with loop"""
    price = int(input())
    amount_free = int(input())
    get_free = int(input())
    demand = int(input())
    new_demand = 0
    free = 0
    while 1:
        new_demand += 1
        if new_demand%amount_free == 0:
            free += get_free
        if free + new_demand >= demand:
            break
    print(new_demand*price, new_demand+free)
main()
