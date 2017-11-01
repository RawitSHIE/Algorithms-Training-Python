"""
pair programing : Rawit& Supakit
date : 14/10/2017
judge: Seq 5
"""
def main(num):
    """count down"""
    while num:
        count = 0
        while count < 7:
            num -= 1
            if num == 0:
                break
            print(num, end=" ")
            count += 1
        if num == 0:
            break
        print()
main(int(input())+1)
