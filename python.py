"""test"""
def main():
    sec = int(input())
    distance = 3.14*2 * 2.5*2.54
    print("%.02f" %(distance*15000 * (sec/60)))
main()
