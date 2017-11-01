"""
judge : Againandagain
pair : Rawit & Aof
date: 5/10/2560
"""
def main():
    """is aeiou"""
    text = input().split()
    listed = []
    for i in text:
        point = 0
        for j in i:
            if j in "a e i o u A E I O U":
                point += 1
                if point == 2:
                    listed.append(i)
                    continue
    listed.sort()
    if len(listed) == 0:
        print("Nope")
    else:
        for i in listed:
            print(i.strip("."))
main()
