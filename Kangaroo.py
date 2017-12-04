"""
Kangaroo
60070081
"""
def main():
    """runtime"""
    lst = []
    for _ in range(3):
        lst += [int(input())]
    if lst[2] - lst[1] > lst[1] - lst[0]:
        print(lst[2]-lst[1]-1)
    elif lst[2] - lst[1] < lst[1] - lst[0]:
        print(lst[1]-lst[0]-1)
    elif lst[2] - lst[1] == lst[1] - lst[0] and lst[1] - lst[0] != 1:
        print(lst[1]-lst[0]-1)
    else:
        print(0)
main()
