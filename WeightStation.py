"""
    JUDGE: WeightStation
    Date: 24 Aug 2017
    Pair: Rawit & Apisit
"""
def main():
    """weight balance and overweight"""
    avg_wheel = float(input())
    wheel_a = float(input())
    wheel_b = float(input())
    wheel_c = float(input())
    weight = 4*avg_wheel
    all_wheel = wheel_a + wheel_b + wheel_c
    wheel_d = weight - all_wheel
    case1 = avg_wheel/2 + avg_wheel >= wheel_a >= avg_wheel/2
    case2 = avg_wheel/2 + avg_wheel >= wheel_b >= avg_wheel/2
    case3 = avg_wheel/2 + avg_wheel >= wheel_c >= avg_wheel/2
    case4 = avg_wheel/2 + avg_wheel >= wheel_d >= avg_wheel/2
    all_case = case1 and case2 and case3 and case4
    if weight <= 15000 and all_case:
        print("Pass", "%.2f" %wheel_d)
    elif weight > 15000:
        print("Overweight")
    else:
        print("Unbalance")
main()
