on_state = False # False -> close, True -> open
warmlight = False # False -> daylight, True -> warmlight
cnt_warm = 0
last_closed = 0
while True:
    on_state = not on_state # Switch State
    tmp = input()
    if tmp.isalpha():
        break

    curr = float(tmp)
    if not on_state: # if is closed, save last closed time and switch light type
        last_closed = curr
        warmlight = not warmlight

    if curr - last_closed >= 6 and on_state: # delay morre than 6 sec and open on_state
        warmlight = False

    if warmlight:
        cnt_warm += 1
print(cnt_warm)