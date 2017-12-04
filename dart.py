"""
dart
60070081
"""
def main():
    """point sep"""
    tmp = int(input())
    point = 0
    for _ in range(tmp):
        rad = radi([int(j) for j in input().split()])
        for i in range(1, 6):
            if rad <= i*2:
                point += 6 - i
                break
    print(point)

def radi(rad):
    """radius"""
    return (rad[0]**2 + rad[1]**2)**0.5
main()
