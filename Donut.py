"""
judge : Donut
pair : Rawit & Aof
date: 5/10/2560
"""
def main():
    """packs"""
    price = int(input())
    amount_free = int(input())
    get_free = int(input())
    demand = int(input())

    #find the number of valueset
    demand_pack = demand // (amount_free+get_free)

    #find the number that won't get extra
    the_rest = demand - demand_pack*(amount_free+get_free)

    if the_rest >= amount_free:
        get = (amount_free+get_free) * (demand_pack+1)
        pay = (demand_pack+1) * amount_free * price

    elif the_rest < amount_free:
        get = ((amount_free+get_free) * demand_pack) + the_rest
        pay = ((demand_pack * amount_free) + the_rest) * price
    print(pay, get)

main()
