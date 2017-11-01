"""
pair programming : 12/10/17
judge: missingcard
"""
def main():
    """key"""
    card = []
    number = ""
    alpha = ""
    for _ in range(51):
        for i in input():
            card.append(i)
    for i in "0123456789JKQA":
        if not card.count(i) == 4:
            number += i
    for i in "SHDC":
        if not card.count(i) == 13:
            alpha += i
    print(number[::-1]+alpha)
main()
