"""
    task run test
    return functionn
"""
def main():
    """print ans"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
    print(func_f(func_f(num_a)))
    print(func_g(func_f(num_a - num_b)))
    print(func_h(func_f(num_a+num_b), func_f(num_a+num_c), func_g(func_f(num_d**2))))
    print(func_i(func_h(func_f(num_a+num_b), func_f(num_a-num_c), func_g(func_f(num_d**2))),\
    func_g(func_f(num_a-num_b)) , func_f(func_f(func_f(func_f(func_f(num_c))))), num_d**8))
def func_f(num_1):
    """function F"""
    return num_1*2

def func_g(num_1):
    """function G"""
    return 3*(num_1**4)-num_1**3+2*(num_1**2)+10

def func_h(num_1, num_2, num_3):
    """function H"""
    return (num_3+num_1)**2-num_1*num_2+num_2**2

def func_i(num_1, num_2, num_3, num_4):
    """function I"""
    return (num_1**2+num_2**2-num_3**2)/(num_4**2-2*num_1*num_4+2*num_1)
main()
