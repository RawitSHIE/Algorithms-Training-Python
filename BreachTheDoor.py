"""
pair programming : 12/10/17
judge: BreachTheDoor
"""
def main():
    """strip special charactar"""
    text = input().split()
    text_i = []
    for i in text:
        text_j = []
        for j in i:
            if j.isalpha():
                text_j.append(j)
        text_j = "".join(text_j)
        if len(text_j) > 6:
            text_i.append(text_j)
    print(" ".join(text_i))
main()
