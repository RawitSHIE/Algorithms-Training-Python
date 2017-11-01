"""
pair programming
recursivefibo
rawit 60070081
"""
def fibo(index):
    """recursive function"""
    if index <= 1:
        return index
    else:
        return fibo(index - 1) + fibo(index - 2)
print(fibo(int(input())))
