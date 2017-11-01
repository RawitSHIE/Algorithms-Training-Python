"""
judge : BlackJack
pair : Rawit & Aof
date: 5/10/2560
"""
def main():
    """find point"""
    point, ace = 0, 0
    num_card = int(input())
    for _ in range(num_card):
        card = input()
        if card in "JKQ":
            point += 10
        elif card == "A":
            ace += 1
        else:
            point += int(card)
    score = point + ace
    if ace:
        while score + 10 <= 21:
            score += 10
    print(score)
main()
