""" Task : Bowling (reddit) """
def chartoint(cha):
    """ character ti integer """
    if cha == '/':
        return 10
    if cha == 'X':
        return 10
    if cha == '-':
        return 0
    return int(cha)
def main():
    """ Scoring a Bowling Game """
    temp = input()
    text = temp.replace(" ", "")
    temp = temp.split(" ")[-1]
    score = [0 for _ in range(10)]
    index = 0
    flame = 0
    while index < len(text)-2+(len(temp) == 2):
        if text[index] != 'X':
            tmp = chartoint(text[index])+chartoint(text[index+1])
            tmp = min(10, tmp)
            if text[index+1] == '/':
                score[flame] = min(30, tmp+chartoint(text[index+2]))
            else:
                score[flame] = min(30, tmp)
            index += 2
        else:
            tmp = chartoint(text[index])
            if text[index+1] == 'X':
                tmp += 10+chartoint(text[index+2])
            else:
                tmp += min(10, chartoint(text[index+2])+chartoint(text[index+1]))
            score[flame] = min(30, tmp)
            index += 1
        flame += 1
    print(sum(score))
main()