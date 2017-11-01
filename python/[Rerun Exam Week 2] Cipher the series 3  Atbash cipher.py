"""Rerun Exam Week 2] Cipher the series :3 - Atbash cipher"""
def main():
    """reversed"""
    text = list(input())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        if i.isalpha():
            code = 0 - (alpha.index(i)+1)
            print(list(alpha)[code], end="")
        else:
            print(i, end="")
main()
