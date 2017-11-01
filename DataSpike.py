"""
    JUDGE: Additive
    Date: 24 Aug 2017
    Pair: Rawit & Apisit
"""
def main():
    """input number"""
    highest = int(input())
    highest = find_highest(highest, int(input()))
    highest = find_highest(highest, int(input()))
    highest = find_highest(highest, int(input()))
    highest = find_highest(highest, int(input()))
    highest = find_highest(highest, int(input()))
    highest = find_highest(highest, int(input()))
    highest = find_highest(highest, int(input()))
    print(highest)
def find_highest(num_a, num_b):
    """compare"""
    return num_a if num_a > num_b else num_b
main()
