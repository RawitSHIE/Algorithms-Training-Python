"""
pair programing : Rawit& Supakit
date : 14/10/2017
judge: Seq 3
"""
def main(num):
    """star at 2"""
    sqe = 0
    for _ in range(num):
        sqe += num
        for i in range(sqe-num, sqe):
            print(i, end=" ")
        print("")
main(int(input()))
