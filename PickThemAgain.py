"""
judge : pickthemagian
pair : Rawit & Aof
date: 5/10/2560
"""
def main():
    """listed"""
    number = input().split()
    thereis = False
    rel_num = []
    for i in number:
        i = int(i)
        if i%3 == 0 or i%5 == 0:
            rel_num.append(i)
            thereis = True
    rel_num.reverse()
    if thereis:
        for i in rel_num:
            print(i)
    else:
        print("Nope")
main()
