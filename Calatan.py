"""
60070081
Catalan
"""
def cala(num):
    """recur"""
    return 1 if num == 1 else cala(num-1)*(4*(num-1) + 2)/((num-1) + 2)
print(int(cala(int(input()))))
