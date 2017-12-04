"""
60070081
kataba
"""
def kataba():
    """debugger"""
    case = []
    for _ in range(int(input())):
        text = input()
        tbakka = text.count("bakka")
        new = text.split("bakka")
        new = "".join(new)
        tta = new.count("ta")
        tba = new.count("ba")
        tka = new.count("ka")
        tbaka = new.count("baka")
        if tbaka:
            case += ["no"]
        elif len(text) == tbakka*5 + tta*2 + tba*2 + tka*2:
            case += ["yes"]
        else:
            case += ["no"]
    for i in case:
        print(i)
kataba()
