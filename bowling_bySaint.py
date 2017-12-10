""" Bowling """

def main():
    """ Main function """
    raw_data = input()
    if len(raw_data.split()[-1]) == 2:
        raw_data += '-'

    scoreboard = convert(list(raw_data.replace(' ', '')))
    score = 0

    for i in range(len(scoreboard)):
        if i >= len(scoreboard)-3:
            #Case: Final frame (No bonus points)
            score += scoreboard[i][1]
        elif scoreboard[i][0] == 'X':
            #Case: Strike
            score += scoreboard[i][1] + scoreboard[i+1][1] + scoreboard[i+2][1]
        elif scoreboard[i][0] == '/':
            #Case: Spare
            score += scoreboard[i][1] + scoreboard[i+1][1]
        else:
            #Case: Normal scorings (and 0)
            score += scoreboard[i][1]

    print(score)

def convert(scoreboard):
    """ Convert scoreboard """
    #If this line of comment still appears, that means you just copy and pasted my code.
    #Well, fuck you copiers. lelelelelelel
    for i in range(len(scoreboard)):
        if scoreboard[i] == 'X':
            scoreboard[i] = ('X', 10)
        elif scoreboard[i] == '-':
            scoreboard[i] = ('-', 0)
        elif scoreboard[i] == '/':
            scoreboard[i] = ('/', 10-scoreboard[i-1][1])
        else:
            scoreboard[i] = (scoreboard[i], int(scoreboard[i]))
    return scoreboard

main()
