"""
60070081
olympics
"""
def main():
    """bad at"""
    dic = {}
    for _ in range(int(input())):
        country = input().split()
        metal = [int(i) for i in country[1:]]
        alm = sum(metal)
        dic[country[0]] = metal + [alm]
    key = sorted(dic)
    item = sorted(dic.values(), reverse=True)
    num = 0
    tmp = []
    count = 0
    for i in item:
        if i == tmp:
            print(num, end=" ")
            count += 1
        else:
            tmp = i
            num += 1 + count
            print(num, end=" ")
            count = 0
        for k in key:
            if dic[k] == i:
                print(k, end=" ")
                key.remove(k)
                break
        for j in i:
            print(j, end=" ")
        print()
main()
