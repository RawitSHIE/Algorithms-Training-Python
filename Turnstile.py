"""
judge : Turnstile
pair : Rawit & Aof
date: 5/10/2560
"""
def main(text=str()):
    """Turnstile Hardcore version"""
    while 1:
        fuc = input()
        if fuc == "END":
            break
        else:
            text += fuc
    print(text.count("CP"))
main()
