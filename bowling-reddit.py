"""
bowling
60070081
"""
def main():
    """hard code"""
    score = input()
    text = score.replace(" ","")
    if len(score.split()[-1]) == 2:
        text += "-"

    tmp = []
    for i in range(len(text)):
        if text[i] == "X":
            tmp += [10]
        elif text[i] == "/":
            tmp += ["/"]
        elif text[i] == "-":
            tmp +=  [0]
        elif text[i].isdigit():
            tmp += [int(text[i])]
    # print(tmp)
    point = []

    for i in range(len(tmp)-3):
        if tmp[i] == 10:
            if tmp[i+2] == "/":
                point += [10 + (10 - tmp[i+1]) + tmp[i+1]]
            else:
                point += [10 + tmp[i+1] + tmp[i+2]]
        elif tmp[i] == "/":
            point += [(10 - tmp[i-1]) + tmp[1+i]]
        else:
            point += [tmp[i]]

    for i in range(len(tmp[-3:])):
        if tmp[-3:][i] == "/":
            point += [(10 - tmp[-3:][i-1])]
        else:
            point += [tmp[-3:][i]]
    # print(point)
    print(sum(point))
main()
