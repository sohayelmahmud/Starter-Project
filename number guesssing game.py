

import random

# game function
def game(number, chances, minimum, maximum):
        # hint calculation
        RANGE_SIZE = maximum - minimum
        HINT = RANGE_SIZE * 0.10
# take guess from user and compare with the ans
        while chances > 0:
            try:
                guess = int(input("Guess the number: "))
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

            if number == guess:
                print("Congratulation! You guessed it right.")
                return

            else:
                chances -= 1
                if chances > 0:
                    if (guess - HINT) > number:
                        print("The guess is too high!")
                    elif guess > number:
                        print("The guess is high!")
                    elif (guess + HINT) < number:
                        print("The guess is too low!")
                    elif guess < number:
                        print("The guess is low!")

                    print(f"You have {chances} chances left. Try again.")
        print(f"You lost! The number was {number} Better luck next time.")


# main program start
print("Welcome to Number Guessing Game")

# main loop for the game
while True:
    chances = 5
    number = 0
    minimum = 1
    maximum = 200

# range set loop for avoid error
    while True:
        try:
            user_input = int(input("Do you want to set the range of number or let me set it for you? \n1. I want to set \n2. You can set: "))
            if user_input in [1,2]:
                break
            else:
                print("Please enter 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")


# user input min & max game start & inside loop for avoiding min-max error
    if user_input == 1:
        while True:
            try:
                minimum = int(input("Set the minimum range of number: "))
                maximum = int(input("Set the maximum range of number: "))
                if minimum >= maximum:
                    print("The minimum number must be strictly less than the maximum number.")
                    continue
                number = random.randint(minimum, maximum)
                print(f"Number set between {minimum} and {maximum}.")
                break
            except ValueError:
                print("Invalid input! Please enter valid whole numbers for the range.")
        # print(number) #.... print testing....................

        game(number, chances, minimum, maximum)

# computer set game start & inside loop for setting difficulty level
    elif user_input == 2:

        while True:
            try:
                difficulty = int(input("Select Difficulty: \n1. Easy (10 Chances, 1-100)\n2. Medium (7 Chances, 1-200)\n3. Hard (5 Chances, 1-500) : "))

                if difficulty in [1, 2, 3]:
                    break
                else:
                    print("Please enter 1, 2, or 3 only.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        if difficulty == 1:
            chances = 10
            maximum = 100
        elif difficulty == 2:
            chances = 7
            maximum = 200
        elif difficulty == 3:
            chances = 5
            maximum = 500

        number = random.randint(1, maximum)
        print(f"Number set between {minimum} and {maximum}. ")
        #print(number)   #.... print for testing...............

        game(number, chances, minimum, maximum)


# play again loop, bake to the main loop or exit
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks for playing. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting a new game.")
            print("................................................................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")