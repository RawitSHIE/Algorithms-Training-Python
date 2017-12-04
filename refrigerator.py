"""Refrigerator"""
def main(amount_food, food):
    """regrigerator"""
    amount_food = 0
    while 0 not in food:
        food = list(map(lambda x: x-1, food))
        food[food.index(min(food))] += 1
        amount_food += 1
    print(amount_food)
main(int(input()), list(map(int, (input().split()))))
