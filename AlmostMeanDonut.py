"""
pair programming
Filter
60070092
"""
def main():
    """the tab"""
    time = int(input())
    student = dict()
    total = 0
    almost = 0
    ind = ""
    for i in range(time):
        listed = input().split("\t")
        student[listed[0]] = listed[1]
        total += float(listed[1])
    mean = total / time
    for i in student:
        if float(student[i]) <= mean and float(student[i]) > almost:
            ind = i
            almost = float(student[i])
    print(ind, almost, sep="\t")
main()
