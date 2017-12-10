"""
PSIT - Week 11
Teerapat Kraisrisirikul (60070183)
"""

def main():
    """ Main function """
    while True:
        otp = input()
        if otp == '0':
            break
        otp = [otp.count(str(i)) for i in range(10)]

        if sum(otp) == 4:
            if otp.count(2) == 1:
                print('valid')
            else:
                print('invalid')
        elif sum(otp) == 6:
            if otp.count(2) == 2 or otp.count(3) == 1:
                print('valid')
            else:
                print('invalid')
        elif sum(otp) == 8:
            if otp.count(3) == 2 or otp.count(2) == 3:
                print('valid')
            else:
                print('invalid')

main()
