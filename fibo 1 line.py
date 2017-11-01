"""
pair programming
recursivefibo
rawit 60070081
"""
def fibo(index):
    """recursive function"""
    return index if index < 2 else fibo(index-1) + fibo(index-2)
print(fibo(int(input())))
