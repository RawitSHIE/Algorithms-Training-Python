"""
pair programing : Rawit& Supakit
date : 14/10/2017
judge: Seq 12
"""
def main(num):
    """super square"""
    for i in range(1, num+1):
        for j in range(num-i, num):
            print("%02d" %(num-(num-j)+1), end=" ")
        for j in range(1, num-i+1):
            print("%02d" %(num-j), end=" ")
        for j in range(num-(num-i)+1, num+1):
            print("%02d"%(j), end=" ")
        for j in range(i-1):
            print("%02d" %(num-j-1), end=" ")
        print()
    for i in range(1, num):
        for j in range(1, num-i+1):
            print("%02d" %abs(num-num-i-j), end=" ")
        for j in range(1, i+1):
            print("%02d"%(num-j), end=" ")
        for j in range(num-i, num):
            print("%02d" %(num-(num-j)+1), end=" ")
        for j in range(1, num-i):
            print("%02d" %(num-j), end=" ")
        print()
main(int(input()))
