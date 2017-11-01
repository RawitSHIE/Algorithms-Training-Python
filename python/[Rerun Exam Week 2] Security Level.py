"""[Rerun Exam Week 2] Security Level"""
def main():
    """secure"""
    time = int(input())
    for _ in range(time):
        data = input().split()
        inval = 1
        pin = list(data[1])
        con1, con2, con3 = 0, 0, 0
        for i in pin:
            if len(pin) < 6:
                inval = 0
            elif i.islower():
                con1 = 1
            elif i.isupper():
                con2 = 1
            elif i.isdigit():
                con3 = 1
            else:
                inval = 0
        sec = (con1 + con2 + con3)*inval
        if sec == 3:
            level = "(Security-Level: High)"
        elif sec == 2:
            level = "(Security-Level: Medium)"
        elif sec == 1:
            level = "(Security-Level: Low)"
        elif sec == 0:
            level = "(Invalid)"
        print("Username:", data[0], "/", "Password:", "*"*len(data[1]), level)
main()
