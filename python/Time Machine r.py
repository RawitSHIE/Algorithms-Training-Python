"""calendar"""
def main():
    """step"""
    month = str(input())
    step = int(input())%12
    almonth = "JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDECJANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC"
    loca = almonth.find(month)
    pos = (loca+2)+((step*3)-2)
    print(almonth[pos:pos+3])
main()
