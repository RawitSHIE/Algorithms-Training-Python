"""
60070081
TheFlood I
"""
def main():
    """greedy"""
    wall = input().split()

    time = 0
    if "0" not in wall:
        while min(wall):
            ind = wall.index(min(wall))
            new = [int(i)-1 for i in wall]
            new[ind] += 1
            wall = new
            time += 1
        print(time)
    else:
        print(0)
main()
