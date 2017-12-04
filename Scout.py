"""
60070081
Scout
"""
def main():
    """eggee"""
    outcome = []
    for i in range(int(input())):
        spec = [int(j) for j in input().split()]

        egg = sorted([int(j) for j in input().split()])

        wei = 0
        count = 0
        for j in egg:
            if wei + j <= spec[2]:
                wei += j
                count += 1
            else:
                break
        outcome += [min(spec[1], count)]
    for i in outcome:
        print(i)

main()
