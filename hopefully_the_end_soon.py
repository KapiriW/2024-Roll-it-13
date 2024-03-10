import random


# checks users enter (y) or (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks ussr responce and questions
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions to the user
def instruction():
    print('''

**** Instructions ****

at the start of each round, the user and the computer each roll two dice. The initial number of points for each player is the total shown by the dice. Then, taking turns, the user and computer each roll a single die and add the result to their points. The goal is to get 13 points (or slightly less) for a given round. Once you are happy with your number of points, you can ‘pass’.

- If you go over 13, then you lose the round (and get zero points).

- If the computer goes over 13, the round ends and your score is the number of points that you have earned.

- If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays the same).

- If you get more points than the computer (but less than 14 points), you win and add your points to your score. The computer’s score stays the same.

- If the first roll of your dice is a double, then your score is increased by double the number of points, provided you win. If the computer’s first roll of the dice is a double, then its points are not doubled (this gives the human player a slight advantage).

- The ultimate winner of the game is the first one to get to the specified score goal.
    ''')


# generates a thing between 0 and 6
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

    # check if we have a double score oppurtunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# Checks that users enter an integer
def int_check(question):
    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input(question))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# finds the lowest, highest and average score from a list
def get_stats(stats_list):
    # sort the lists.
    stats_list.sort()

    # find lowest, highest and average scores...
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# main routine goes here

# initialise user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

# create lists to hold user scores, computer scores and game history
user_scores = []
comp_scores = []
game_history = []

# Program starts here (with a heading)
print()
print("  Roll it 13  ")
print()

# Display instructions if user wants to see them.
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# Get target score (must be an integer more than 13)
print()
target_score = int_check("Enter a target score: ")
print()


# Loop game until we have a winner
while user_score < target_score and comp_score < target_score:
    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"  Round {num_rounds} ")

    # Start of a single round

    # initialise 'pass' variables
    user_pass = "no"
    computer_pass = "no"

    # Start Round...
    print("Press <enter> to begin this round: ")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    # print(f"The computer rolled a total of {computer_points}.")

    # Loop (while both user / computer have <= 13 points)...
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update
        # points / status
        print()

        # If user has 13 points, we can assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # If user goes over 13 points, tell them that they lose and set points to 0


            if user_points > 13:
                print(f"  Oops! You rolled a {user_move} so your total is {user_points}.  "
                      f"Which is over 13 points . ")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}.")

        else:
            # If user passes, we don't want to let them roll again!
            user_pass = "yes"

        # if computer has 10 points or more (and is winning), it should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop.
        elif computer_pass == "yes":
            pass

        else:

            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # check computer has not gone over the limit
            if computer_points > 13:
                print(f" The computer rolled a {computer_move}, taking their points"
                      f" to {computer_points}.  This is over 13 points so the computer loses! ")
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}.  The computer"
                      f" now has {computer_points}.")

        print()
        if user_points > computer_points:
            result = " You are ahead. "
        elif user_points < computer_points:
            result = "  The computer is ahead!  "
        else:
            result = " It's currently a tie. "

        print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

    # if both the user and the computer have passed,
        # we need to exit the loop.
        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside rounds loop - double user points if  won and are eligible

    # Show rounds result
    print()

    if user_points < computer_points:
        print("  Sorry - you lost this round and no points "
              "have been added to your total score.  The computer's score has "
              f"increased by {computer_points} points.")

        add_points = computer_points

# currently does not include double points!
    elif user_points > computer_points:
    # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print(f" Yay!  You won the round and {user_points} points have "
              f"been added to your score ")

        add_points = user_points

    else:
        print(f"  The result for this round is a tie.  You and the computer "
              f"both have {user_points} points.	")

        add_points = user_points

    # Record round result and add it to the game history
    round_result = f"Round {num_rounds} - User: {user_points} \t Computer: {computer_points}"
    game_history.append(round_result)

    # end of a single round

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        comp_score += add_points

    # if the user wins, add their points to their score
    elif user_points > computer_points:

        user_score += add_points

    # if it's a tie, add the points to BOTH SCORES
    else:

        comp_score += add_points
        user_score += add_points

    user_scores.append(user_score)
    comp_scores.append(comp_score)

    print()
    print(f" User: {user_score} points | Computer: {comp_score} points  ")
    print()

print()

# Display the  winner and score info.
print()
if user_score > comp_score:
    print(" Game Over - You Won ")
elif user_score < comp_score:
    print("!!! Game Over - You Lost !!!")
else:
    print("@@@ Game Over - It's a Tie @@@")

print(f"Final Scores: User ({user_score}) vs Computer ({comp_score})")
print()

# Display game history if user wants to see it

show_history = yes_no("Would you want to see the game history?")

if show_history == "yes":
    print("\n⌛⌛⌛ game history⌛⌛⌛")

    for item in game_history:
        print(item)

print()

# calculate the lowest highest and average
# scores and show them.

user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

print("###   Game Statistics ### ")
print(f"User  - Lowest Score: {user_stats[0]}\t "
      f"Highest Score: {user_stats[1]}\t "
      f"Average Score: {user_stats[2]:.2f}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t "
      f"Highest Score: {comp_stats[1]}\t "
      f"Average Score: {comp_stats[2]:.2f}" )

print()
print("Thanks for playing the game." )
