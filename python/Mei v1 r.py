"""combo kill"""
def main():
    """Mei damage and combo strike"""
    damage = int(input())
    health = int(input())
    if damage >= 80 and damage + 75 >= health:
        print("Solo_Kill")
    elif damage >= 80:
        print(damage + 75)
    else:
        print(damage)
main()
