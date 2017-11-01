"""
pair programing : Rawit& Supakit
date : 14/10/2017
judge: Seq 11
"""
def main(num):
    """super square"""
    for i in range(1, num+1):
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for _ in range(1, num-i+1):
            print("%02d"%i, end=" ")
        for _ in range(1, num-i+1):
            print("%02d"%i, end=" ")
        for j in range(1, i):
            print("%02d" %(i-j), end=" ")
        print()
    for i in range(1, num):
        for j in range(1, num-i+1):
            print("%02d" %j, end=" ")
        for j in range(1, i+1):
            print("%02d"%(num-i), end=" ")
        for _ in range(1, i+1):
            print("%02d"%(num-i), end=" ")
        for j in range(1, num-i):
            print("%02d" %(num-j-i), end=" ")
        print()
main(int(input()))
