"""
date : 21/09/2560
pair pro: Rawit & Supakit
judge : Divided3Or5
"""
def main():
    """number 1"""
    num = 0
    for i in range(1, int(input())+1):
        if i%3 == 0 or i%5 == 0:
            num += i
    print(num)
main()
