"""
test run

"""
def main():
    """bowling"""
    sheet = input()
    tmp = sheet.split()[-1]
    raw = sheet.replace(" ","")
    if len(tmp) == 2:
        raw += '-'

    print(list(raw))

    convert = []
    for i in raw:
        if i == "X":
            convert += [10]
        elif i == "/":
            convert += "/"
        elif i == "-":
            convert += [0]
        elif i.isdigit():
            convert += [int(i)]
    print(convert)

    point = []
    for i in range(len(convert)-3):
        if convert[i] == 10:
            if convert[i+2] == "/":
                point += [10 + convert[i+1] + (10 - convert[i+1])]
            else:
                point += [convert[i+1] + convert[i+2] + 10]

        elif convert[i] == "/":
            point += [(10 - convert[i-1]) + convert[i+1]]

        else:
            point += [convert[i]]

    for i in range(len(convert[-3:])):
        if convert[-3:][i] == "/":
            point += [10 - convert[-3:][i-1]]
        else:
            point += [convert[-3:][i]]

    print(sum(point))
main()