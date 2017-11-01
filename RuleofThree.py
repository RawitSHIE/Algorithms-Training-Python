"""
date : 21/09/2560
pair pro: Rawit & Supakit
judge : RuleofThree
"""
def main():
    """num compare"""
    num_d, num_d2 = 1, 0
    for _ in range(int(input())):
        num = float(input())
        num2 = float(input())
        if num2/num == num_d2/num_d and num2 < num_d2:
            num_d = num
            num_d2 = num2
        elif num2/num > num_d2/num_d:
            num_d = num
            num_d2 = num2
    print("%.2f %.2f" %(num_d, num_d2))
main()
