"""
60070081
CaesarV2
"""
def shift():
    """shift"""
    stg = ""
    for i in input():
        if chr(ord(i)-3).isalpha() and i.isalpha():
            stg += chr(ord(i)-3)
        elif i.islower():
            stg += chr(123 - (97 - (ord(i)-3)))
        elif i.isupper():
            stg += chr(91 - (65 - (ord(i)-3)))
        else:
            stg += i
    print(stg)
shift()
