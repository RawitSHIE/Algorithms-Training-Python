"""Fibonacci number V.1"""
def main():
    """ number V.1 """
    num = int(input())
    retu = 0
    fibo = [0, 1]
    for _ in range(num):
        retu = fibo[-1] + fibo[-2]
        fibo.append(retu)
    print(fibo[num])
main()
