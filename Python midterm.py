"""def main"""
def main():
    """test algorithum"""
    text = ""
    for _ in range(16):
        mother = input()
        text += mother
    for i in range(10):
        if str(i) in text:
            locate = text.index(str(i))
            fucker_x = bin(locate%16)
            fucker_y = bin(locate//16)
            print("%04d%04d # <--- %d\'s Position" %(int(fucker_y[2:]), int(fucker_x[2:]), int(i)))
main()
