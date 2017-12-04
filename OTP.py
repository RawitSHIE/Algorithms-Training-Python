"""
OTP
60070081
"""
def main():
    """encoding"""
    case = []
    while True:
        text = input()
        if text == "0":
            break
        else:
            if len(text) == 4:
                case += [compat_4(text)]
            elif len(text) == 6:
                case += [compat_6(text)]
            elif len(text) == 8:
                case += [compat_8(text)]
    for i in case:
        print(i)


def compat_4(text):
    """4 len"""
    lst = []
    for i in "0123456789":
        if i in text:
            lst += [text.count(i)]
    return "Valid" if len(lst) == 3 else "Invalid"

def compat_6(text):
    """6 len"""
    lst = []
    for i in "0123456789":
        if i in text:
            lst += [str(text.count(i))]
    if lst.count("3") == 1 and lst.count("2") == 0 and lst.count("1") == 3 and len(lst) == 4:
        return "Valid"
    elif lst.count("2") == 2 and lst.count("1") == 2 and len(lst) == 4:
        return "Valid"
    else:
        return "Invalid"

def compat_8(text):
    """8 len"""
    lst = []
    for i in "0123456789":
        if i in text:
            lst += [str(text.count(i))]
    if lst.count("3") == 2 and lst.count("2") == 0 and lst.count("1") == 2 and len(lst) == 4:
        return "Valid"
    elif lst.count("2") == 3 and lst.count("1") == 2 and len(lst) == 5:
        return "Valid"
    else:
        return "Invalid"

main()
