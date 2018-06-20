"""
Shut the box
============


"""

import random as rnd
import time
import sys
import box

# stop execution if not enough inputs
if len(sys.argv) != 3:
    print("not enought command line arguments")
    quit()
# get player's name
player = sys.argv[1]
# get game max seconds
secs_string = sys.argv[2]
secs = int(secs_string)

# initial list of boxes
remaining = list(range(1, 10, 1))
time0 = time.time()
timediff = 0

while secs - timediff > 0:
    print("Numbers left = ", remaining)
    if sum(remaining) <= 6:
        roll = rnd.randint(1, 6)
    else:
        roll = rnd.randint(1, 6) + rnd.randint(1, 6)
    print("Roll = ", roll)
    if not box.isvalid(roll, remaining):
        print("Game over!")
        quit()
    timediff = time.time() - time0
    print("Seconds left = ", secs - timediff )
    inputs = False
    while inputs == False:
        player_input = input("Numbers to eliminate = ")
        parsed_input = box.parse_input(player_input, remaining)
        if parsed_input:
            if sum(parsed_input) == roll:
                for i in range(1, len(parsed_input) + 1):
                    remaining.remove(parsed_input[i-1])
                inputs = True
            else:
                print("invalid input")
        else:
            print("invalid input")
    print("")
    if not remaining:
        print("Score for player ", player, ": 0 points")
        print("Time played = ", timediff," seconds")
        print("Congratulations!! You shut the box!")
        quit()

print("Game over!")
