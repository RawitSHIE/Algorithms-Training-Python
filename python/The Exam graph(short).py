"""The Exam graph(short)"""
def main():
    """graph"""
    time = int(input())
    name, full2 = [], []
    for _ in range(time):
        full = input()
        full2.append(full)
    full3 = sorted(full2)
    for i in range(time):
        full4 = full3[i].split()
        for _ in range(1):
            name = full4[0]
            score = full4[1]
        print("%10s:" %name, "*"*(int(score)//5))
main()
