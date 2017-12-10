"""
PSIT - Week 12
Teerapat Kraisrisirikul (60070183)
WARNING: DO NOT copy and submit my code.
"""

def main():
    """ Main function """
    var_p, var_q, var_r = int(input()), int(input()), int(input())
    matrice_a = [[int(input()) for _ in range(var_q)] for _ in range(var_p)]
    matrice_b = [[int(input()) for _ in range(var_r)] for _ in range(var_q)]
    matrice_new = [[None for _ in range(var_r)] for _ in range(var_p)]

    for i in range(var_p):
        for j in range(var_r):
            matrice_new[i][j] = calculate(matrice_a, matrice_b, i, j)

    for i in range(len(matrice_a)):
        for j in range(len(matrice_b[0])):
            print(matrice_new[i][j], end=' ')
        print()

def calculate(matrice_a, matrice_b, digit_i, digit_j):
    """ Calculate a row and column of matrice """
    row = [matrice_a[digit_i][j] for j in range(len(matrice_a[0]))]
    col = [matrice_b[i][digit_j] for i in range(len(matrice_b))]

    total = 0
    for i in range(len(row)):
        total += row[i]*col[i]
    return total
    #lelelelelel

main()
