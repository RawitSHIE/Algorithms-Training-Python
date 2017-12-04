"""
600700081
RockPaperScissor
"""
def main():
    """win drow"""
    game = input()
    point = []
    for i in range(1, len(game)+1, 2):
        point += [time(game[i-1], game[i])]
    a_p = point.count("a")
    b_p = point.count("b")
    if a_p > b_p:
        print("A win %d-%d" %(a_p, b_p))
    elif a_p < b_p:
        print("B win %d-%d" %(b_p, a_p))
    if a_p == b_p:
        print("DRAW %d" %a_p)


def time(aaa, bbb):
    """condition"""
    if aaa == bbb:
        return "d"
    elif aaa == "R":
        return "a" if bbb == "S" else "b"
    elif aaa == "P":
        return "a" if bbb == "R" else "b"
    elif aaa == "S":
        return "a" if bbb == "P" else "b"

main()
