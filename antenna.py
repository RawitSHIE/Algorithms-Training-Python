"""
antenna
60070081
"""
import json
def main():
    """radius"""
    rad = int(input())*2
    loc = sorted(json.loads(input()))
    if len(loc) != 0:
        edge = loc[0]
        bss = 1
        for i in loc:
            if i - edge > rad:
                bss += 1
                edge = i
        print(bss)
    else:
        print(0)
main()
