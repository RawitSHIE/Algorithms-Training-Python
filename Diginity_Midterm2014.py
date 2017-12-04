"""
Diginity_Midterm2014
60070081
"""
def main():
    """7 segment"""
    listed = []
    while True:
        num = str(input())
        if num == "0":
            break
        else:
            listed += [encode(num)]
    for i in listed:
        print(i)

def encode(num):
    """encode"""
    while True:
        if len(num) > 1:
            num = str(sum([int(i) for i in num]))
        else:
            return num

main()
