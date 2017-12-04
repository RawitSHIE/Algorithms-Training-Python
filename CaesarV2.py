"""
60070081
CaesarV2
"""
def shift():
    stg = ""
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in input():
        if i in alp or i in alp.lower():
            stg += chr(ord(i)-3)
        else:
            stg += "i"
    print(stg)
shift()
