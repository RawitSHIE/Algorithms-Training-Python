"""
PSIT - Review
Date: 5th December 2017
By: Teerapat K.
NOTE: DO NOT COPY!
"""

import math

def main():
    """ Main fuction """
    distance, slowtime = 0, 0
    price = 0

    #Inputs
    while True:
        drive = input().split()
        if drive[0] == 'F':
            break
        if drive[0] == 'K':
            distance += int(drive[1])
        elif drive[0] == 'W':
            slowtime += int(drive[1])
            distance += int(drive[2])

    #Calculation
    price += (slowtime*1.5)//2*2

    if distance > 80:
        price += (distance-80)*8.5
        distance = 80
    if distance > 60:
        price += (distance-60)*7.5
        distance = 60
    if distance > 40:
        price += (distance-40)*6.5
        distance = 40
    if distance > 20:
        price += (distance-20)*6
        distance = 20
    if distance > 12:
        price += (distance-12)*5.5
        distance = 12
    if distance > 1:
        price += (distance-1)*5
        distance = 1

    price += 35                 #Starting money
    price = math.ceil(price)    #Ceil up
    price += price % 2 == 0     #Add if it's even number

    print(int(price))

main()
