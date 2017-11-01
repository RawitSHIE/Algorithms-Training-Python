"""Count the point V.1"""
def main():
    """Count the point V.1"""
    time = int(input())
    for _ in range(time):
        point = list(input())
        if "." in point:
            num = point.index(".")
            print(len(point[num+1:]))
        else:
            print(0)
main()
