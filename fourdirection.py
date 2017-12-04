"""
four direction
60070081
"""
def main():
    """the arrow"""
    sqe = input()
    a_u = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
    a_d = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
    a_l = ["  *  ", " *   ", "*****", " *   ", "  *  "]
    a_r = ["  *  ", "   * ", "*****", "   * ", "  *  "]
    for i in range(5):
        for j in sqe:
            if j == "U":
                print(a_u[i], end=" ")
            elif j == "D":
                print(a_d[i], end=" ")
            elif j == "L":
                print(a_l[i], end=" ")
            elif j == "R":
                print(a_r[i], end=" ")
        print(" ")
main()
