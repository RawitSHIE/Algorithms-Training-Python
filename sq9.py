"""
pair programing : Rawit& Supakit
date : 14/10/2017
judge: Seq 9
"""
def main(num):
    """repeat"""
    for i in range(1, num+1):
        print(" "*abs((num*3)-i*3), end="")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for j in range(1, i):
            print("%02d" %(i-j), end=" ")
        print()
main(int(input()))
