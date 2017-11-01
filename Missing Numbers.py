"""
pair programming
Filter
rawit 60070081
"""
def main():
    """removing"""
    listed = int(input())
    created = []
    for i in range(1, listed+1):
        created.append(i)
    while True:
        num = int(input())
        if num == 0:
            for i in created:
                print(i)
            break
        created.remove(num)
main()
