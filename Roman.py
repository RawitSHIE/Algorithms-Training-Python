"""
Roman
60070081
"""
def main():
    """base 10"""
    lst = list(input())
    convert = []
    for i in lst:
        if i == "M":
            convert += [1000]
        elif i == "D":
            convert += [500]
        elif i == "C":
            convert += [100]
        elif i == "L":
            convert += [50]
        elif i == "X":
            convert += [10]
        elif i == "V":
            convert += [5]
        elif i == "I":
            convert += [1]

    convert += [0]
    # print(convert)
    real = 0
    dele = 0
    for i in range(len(convert)-1):
        if convert[i] >= convert[i+1]:
            real += convert[i] - dele
            dele = 0
        else:
            dele += convert[i]
            # print(dele)
    print(real)

main()
