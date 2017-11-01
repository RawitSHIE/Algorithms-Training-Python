"""[Rerun Exam Week 2] Count type :3"""
def main():
    """count type"""
    text = list(input())
    lower, upper, digit = [], [], []
    for i in text:
        if i.islower():
            lower.append(i)
        elif i.isupper():
            upper.append(i)
        elif i.isdigit():
            digit.append(i)
    print("Upper :", len(upper))
    print("Lower :", len(lower))
    print("Number :", len(digit))
main()
