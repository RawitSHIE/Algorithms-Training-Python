"""
ProgressiveTax_Midterm2014
60070081
"""
def main():
    """submarine"""
    income = int(input())
    tax = 0

    listed = [0, 150000, 300000, 500000, 750000, 1000000, 2000000, 4000000]
    chrted = [0, 5, 10, 15, 20, 25, 30, 35]
    for i, j in zip(listed[::-1], chrted[::-1]):
        if income > i:
            tax += abs(income-i)*j/100
            income -= abs(income - i)
    print(int(tax))
main()
