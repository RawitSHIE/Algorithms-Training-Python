"""Recur"""
def main(number, memo):
    """THis is main"""
    print(recur(number, memo))
def recur(num, mem):
    """THis is recursion"""
    if num > 500:
        recur(num-500, mem)
    if num not in mem:
        mem[num] = recur(num-1, mem)+recur(num-2, mem)
    return mem[num]
main(int(input()), {0:0, 1:1})