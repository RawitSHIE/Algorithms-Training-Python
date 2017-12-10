"""
60070081
KATABA
"""
def main():
    """lang"""
    text = input()
    print(cur(text))

def cur(text):
    """check"""
    while True:
        if text[:2] == "ta" or text[:2] == "ka":
            text = text[2:]
        elif text[:5] == "bakka":
            text = text[5:]
        elif text[:2] == "ba" and text[:4] != "baka":
            text = text[2:]
        else:
            return "no"
    return "yes"
main()
