"""
pair programing : Rawit& Supakit
date : 14/10/2017
judge: Seq 6
"""
def main(num):
    """PYRAMID"""
    for i in range(1, num+1):
        for j in range(1, i):
            print(j, end=" ")
        print(i)
    for i in range(1, num):
        for j in range(1, num-i):
            print(j, end=" ")
        print(num-i)
main(int(input()))
