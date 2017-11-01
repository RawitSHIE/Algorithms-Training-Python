"""
    pair programming : SceneSwitch I
    name : Rawit & Pair
    Date : 1 / 9 / 2560
"""
def main():
    """light must go on"""
    light_on = False
    warm_state = False
    pre_time = 0
    warm_count = 0
    while 1:
        light_on = not light_on #switch
        #---------input check-----------#
        tim_current = input()
        if tim_current.isalpha(): #check if alpha
            break
        tim_current = float(tim_current)
        #----------calculation part----------#
        if not light_on:
            warm_state = not warm_state #switch to cold state and warm state
            pre_time = tim_current
        if tim_current - pre_time > 6 and light_on:#6 sec condition
            warm_state = False
        if warm_state and light_on:#count warm state
            warm_count += 1
    print(warm_count)
main()
 