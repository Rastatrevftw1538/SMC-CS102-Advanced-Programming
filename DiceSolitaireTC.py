# Trevor Cardoza
# CS 102 Spring 2020
# Febuary 20th
# Program: DiceSolitare.
# A solitare game that you roll or hold to get summed points
# until you hold. The goal is to reach the goal in as little
# turns as possible.

import random

# Main program


def main():
    goal = 50
    score = 0
    turn_score = 0
    turns = 0
    # Greeting and instructions.
    print("\nWelcome to Dice Solitare!")
    print(
        f"\nthe goal is to reach {goal} points in as little turns as possible.")
    print(f"\nYour total score is {score}")
    # This handles the first roll which is automatic.
    dice1 = random.randrange(1, 6)
    dice2 = random.randrange(1, 6)
    sum_of_dice = dice1 + dice2
    turn_score += sum_of_dice
    if sum_of_dice == 2 or sum_of_dice == 7 or sum_of_dice == 12:
        print(f"\nYour first roll is {dice1} and {dice2}\n")
        print("Busted! you lost all your turn points")
        print(
            f"After 1 turn you have a total of {score}!\n")
        turn_score = 0
    else:
        print(f"\nYour first roll is {dice1} & {dice2}")
        print(f"your turn points are {turn_score}\n")

    # This checks for if the goal was reached.
    while score <= goal:
        # This is to restart the round.
        while True:
            choice = str(input("roll or hold? (R/H): "))
            # This section does the processes for when you roll.
            if choice == "r":
                dice1 = random.randrange(1, 6)
                dice2 = random.randrange(1, 6)
                sum_of_dice = dice1 + dice2
                turn_score += sum_of_dice
                if sum_of_dice == 2 or sum_of_dice == 7 or sum_of_dice == 12:
                    print(f"\nYour next roll is {dice1} & {dice2}\n")
                    print("Busted! you lost all your turn points")
                    print(
                        f"After {turns} turns you have a total score of {score}!\n")
                    turn_score = 0
                    break
                else:
                    print(f"\nYour next roll is {dice1} & {dice2}")
                    print(f"your turn points are {turn_score}\n")
                    break
            # This section does the processes for when you hold.
            if choice == "h":
                turns += 1
                score += turn_score
                print(
                    f"\nAfter {turns} turns you have a total score of {score}!\n")
                break
            # This is for if you enter anything else.
            else:
                print("\nPlease type R or H!")

    # This is for when you reach the score goal and the program ends.
    print(f"\nCongratulations! You Won!")
    print(f"It took you {turns} turns!")


# Starts the main program.
main()
