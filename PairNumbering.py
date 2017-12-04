"""
60070081
PairNumbering
"""
import json
def main():
    """timeout"""
    list_a = sorted(json.loads(input()))
    list_b = sorted([str(i) for i in json.loads(input())])
    point = 0
    num_p = int(input())
    for i in list_a:
        if i > num_p:
            break
        point += list_b.count(str(num_p - i))
    print(point)
main()
