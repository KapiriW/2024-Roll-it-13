import random


# generates an integer between 0 and 6
# to simulate a roll of a die

def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total and whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1:{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# main routine goes here

# initialize 'pass' variables
user_pass = "no"
computer = "no"

# get initial dice rolls for user
user_first = two_rolls("User")
user_points = user_first[0]
double_points = user_first[1]

user_move = ""
# Tell the user if they are eligible for double points
if double_points == "yes":
    print("If you win this round, you gain double points")

else:
    double_feedback = "If you win this round, you gain double points!"
# output initial move results
# print(f"you rolled a total of {user_points}. {double_feedback}")
# print()


# get initial dice rolls for computer
computer_first = two_rolls("Computer")
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")
# Loop (while both user / computer have <= 13 points)...
while computer_points < 13 and user_points < 13:
    # ask user if they want to roll again, update
    # points / status
    print()
    if user_pass == "no":
        roll_again = input("Do you want to roll the dice(type 'no' to pass): ")
    else:
        roll_again = "no"

    if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move
            print(f"You rolled a {user_move}. you now have {user_points} points.")

    else:
        # if user passes we dont let them roll again!
        user_pass = "yes"

    # roll die for computer and update computer points
    # when user is over 13 points they lose

    if user_points > 13:
        print(f"Oops! you rolled a {user_move} so your total is {user_points}. "
              f"which is over 13 points so you lose this round and "
              f"don't get any points added to your total score.")

        # reset user points to zero so that when we update their
        # score at the end of round it is correct.
        user_points = 0

        break

    else:
        print(f"You rolled a {user_move} amd have a total score of {user_points}." )
    # if computer is 10 or more
    if computer_points >= 10 and computer_points >= user_points:
        computer_pass = "yes"

    else:
        # roll die for computer and update computer points
        computer_move = roll_die()
        computer_points += computer_move
        # check computer has not gone over
        if computer_points > 13:
            print(f"🌙🌙🌙 the computer rolled a {computer_move}, taking their points"
                  f" to {computer_points}. this is over 13 points so the computer loses 🌙 🌙 🌙")
            computer_points = 0
            break

        else:
            print(f"The computer rolled a {computer_move}. the computer"
                      f" now has {computer_points}")
    # show user results of latest move
    print()
    if user_points > computer_points:
        result = "😀😀😀You are ahead.😀😀😀"
    elif user_points < computer_points:
        result = "😅😅😅The computer is ahead!😅😅😅"
    else:
        result = "😡😡😡Its currently a tie😡😡😡"

    print(f"***Round Update****: {result} ")
    print(f"User score: {user_points} \t | \t Computer Score: {computer_points}")

    print()
    if computer_pass == "yes" and user_pass == "yes":
        break


# Show rounds result
if user_points < computer_points:
    print("Sorry - you lost this round and no points "
          "have been added to your total score. The computer's score has "
          f"increased by {computer_points} points.")
elif user_points > computer_points:
    # outside loop - double user points if they won and are eligible
    if double_points == "yes":
        user_points *= 2

        print(f"Yay! You won the round and {user_points} points have "
              f"been added to your score")
else:
    print(f"the result for this round is a tie. you and the computer"
          f" both have {user_points} ")