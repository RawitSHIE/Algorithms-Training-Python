"""
PSIT - Week 13
Teerapat Kraisrisirikul (60070183)
with his help
"""

def main():
    """ Main function """
    text = input()
    topgram = [None, 0]

    for i in range(len(text)-1):
        if i == len(text)-2:
            check = text[i::]
        else:
            check = text[i:i+2]

        if run_check(text, check) > topgram[1]:
            topgram = [check, run_check(text, check)]

    print(topgram[0], topgram[1], sep='\n')

def run_check(text, check):
    """ Run check """
    count = 0
    for i in range(len(text)-1):
        if i == len(text)-2:
            count += text[i::] == check
        else:
            count += text[i:i+2] == check
    return count

main()
