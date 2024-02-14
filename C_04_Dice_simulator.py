import random


# generates an integer between 0 and 6
# to simulate a dice roll
def roll_die():
    result = random.randint( 1, 6)
    return result
# main routine goes here
die_roll = roll_die()
print(die_roll)