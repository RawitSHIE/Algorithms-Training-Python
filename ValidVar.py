"""
ValidVar
60070081
"""
def main():
    """restriction word"""
    alo = []
    for _ in range(int(input())):
        key = input()
        wreck = False
        if " "+key.strip()+" " in " if else elif while for True False continue break \
        return is in and or from as pass not def None ":
            wreck = True

        elif key[0] in "0123456789":
            wreck = True

        elif " " in key.strip(" "):
            wreck = True

        for i in key.strip():
            if not (i.isalpha() or i == "_" or i.isdigit()):
                wreck = True
                break

        if wreck:
            alo += ["Invalid"]
        else:
            alo += ["Valid"]

    for i in alo:
        print(i)
main()
