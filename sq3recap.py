"""sq3"""
def main():
    """s13"""
    text = ""
    for _ in range(16):
        text += input()
    for i in range(10):
        if i in text:
            loca = text.index(str(i))
            x = loca % 16 
            y = loca // 16
            print("%04d%04d # <--- %d\'s Position" %(int(y[2:]), int(x[2:]), int(i)))
main()
