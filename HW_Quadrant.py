"""
HW_Quadrant
60070081
"""
def main():
    """locate"""
    xxx = int(input())
    yyy = int(input())
    if not xxx and not yyy:
        print("O")
    elif xxx == 0:
        print("Y")
    elif yyy == 0:
        print("X")
    elif xxx > 0 and yyy > 0:
        print("Q1")
    elif xxx > 0 and yyy < 0:
        print("Q4")
    elif xxx < 0 and yyy > 0:
        print("Q2")
    elif xxx < 0 and yyy < 0:
        print("Q3")
main()
