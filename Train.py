"""train"""
def main():
    """the platform"""
    station_a = input()
    station_b = input()
    a_alpha = station_a[:spliter(station_a)]
    a_digit = int(station_a[spliter(station_a):])
    b_alpha = station_b[:spliter(station_b)]
    b_digit = int(station_b[spliter(station_b):])
    digit = abs(a_digit-b_digit)
    alpha = abs(base26(a_alpha) - base26(b_alpha))
    print(digit)
    print(alpha)

def spliter(station):
    index_a = 0
    for i in station:
        if i.isdigit():
            break
        index_a += 1
    return index_a

def base26(alpha):
    base_26 = 0
    power = 1
    for i in alpha:
        loca = int("ABCDEFGHIGKLMNOPQRSTUVWXYZ".index(i))
        base_26 += (loca*(26**(len(alpha)-power)))
        power += 1
    return base_26


main()
