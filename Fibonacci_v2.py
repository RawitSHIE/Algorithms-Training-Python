"""
pair programming : 12/10/17
judge: Fibonacci_v2
"""
def main():
    """bubling"""
    cons_1 = 0
    cons_2 = 1
    num = int(input())
    if num >= 30:
        for _ in range(num):
            num3 = cons_2 + cons_1
            cons_1 = cons_2
            cons_2 = num3
        print(cons_1)
main()
