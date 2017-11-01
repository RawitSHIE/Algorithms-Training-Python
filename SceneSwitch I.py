"""
    pair programming : SceneSwitch I
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main():
    """switch scence"""
    switch_state = 0
    warm_state = 0
    light_state = 1
    timeig = 0
    while 1:
        current_timig = input()
        if current_timig.isalpha():
            break
        current_timig = float(current_timig)
        if switch_state%2 == 0:
            #if light_state%2 == 1: #and current_timig - timeig <= 6:
            if current_timig - timeig <= 6:
                light_state += 1
                if light_state%2 == 1:
                    warm_state += 1
        timeig = current_timig
        switch_state += 1
        #print("warm:",warm_state)
        #print("light",light_state)
        #print("switch:",switch_state)
    print(warm_state)
main()
