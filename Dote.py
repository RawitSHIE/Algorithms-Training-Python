"""
60070081
Dot_E
"""
def main():
    """dota"""
    per = int(input())
    if per%2 == 1:
        per += 1

    team = fac(per)/(fac(per/2)*fac(per/2))
    print(int(team))

def fac(num):
    """fac"""
    count = 1
    for i in range(1, int(num)+1):
        count *= i
    return count
main()
