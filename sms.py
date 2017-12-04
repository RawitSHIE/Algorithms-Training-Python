"""
sms
60070081
"""
def main():
    """tele"""
    stg = ""
    qwerty = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    for _ in range(int(input())):
        num = int(input())
        if num == 1:
            sqe = int(input())
            stg = stg[:max(0, len(stg)-sqe)]
        elif num == 7 or num == 9:
            stg += qwerty[num-1][(int(input())-1)%4]
        else:
            stg += qwerty[num-1][(int(input())-1)%3]
    if stg == "":
        print("null")
    else:
        print(stg)
main()
