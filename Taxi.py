"""
Taxi
60070081
"""
import math
def main():
    """grab and uber"""
    text = []
    while True:
        tmp = input()
        if tmp == "F":
            break
        else:
            text += [tmp.split()]
    rang = 0
    time = 0
    for i in text:
        if len(i) == 2:
            rang += int(i[1])
        else:
            rang += int(i[2])
            time += int(i[1])
    rang = run(rang)

    wait = (time*1.5)//2 * 2
    rang = math.ceil(rang)
    rang += rang%2 == 0

    print(int(wait+rang))

def run(leng):
    """run dis"""
    price = 0
    dis = int(leng)
    if dis > 80:
        price += (dis-80)*8.50
        dis = 80
    if dis > 60:
        price += (dis-60)*7.50
        dis = 60
    if dis > 40:
        price += (dis-40)*6.50
        dis = 40
    if dis > 20:
        price += (dis-20)*6
        dis = 20
    if dis > 12:
        price += (dis-12)*5.50
        dis = 12
    if dis > 1:
        price += (dis - 1)*5
        dis = 1
    price += 35
    return price


main()
