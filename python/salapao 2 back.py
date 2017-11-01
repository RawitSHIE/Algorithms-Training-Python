"""salapao"""
def main():
    """..."""
    xmid = float(input())
    ymid = float(input())
    rad = float(input())
    xpo = float(input())
    ypo = float(input())
    xdel = (xpo <= (xmid + rad)) and (xpo >= (xmid - rad))
    ydel = (ypo <= (ymid + rad)) and (ypo >= (ymid - rad))
    todel = xdel and ydel
    if todel:
        print("Yess!")
    else:
        print("Noo!")
main()
