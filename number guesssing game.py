# will fix bug for valuerror,

import random

def game(number, chances = 5):
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
                    if (guess - 20) > number:
                        print("The guess is too high!")
                    elif guess > number:
                        print("The guess is high!")
                    elif (guess + 20) < number:
                        print("The guess is too low!")
                    elif guess < number:
                        print("The guess is low!")

                    print(f"You have {chances} chances left. Try again.")
        print("You lost! Better luck next time.")


print("Welcome to Number Guessing Game")


while True:
    chances = 5
    number = 0
    while True:
        try:
            user_input = int(input("Do you want to set the range of number or let me set it for you? \n1. I want to set \n2. You can set: "))
            if user_input in [1,2]:
                break
            else:
                print("Please enter 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")



    if user_input == 1:
        while True:
            try:
                minimum = int(input("Set the minimum range of number: "))
                maximum = int(input("Set the maximum range of number: "))
                if minimum >= maximum:
                    print("The minimum number must be strictly less than the maximum number.")
                    continue
                number = random.randint(minimum, maximum)
                break
            except ValueError:
                print("Invalid input! Please enter valid whole numbers for the range.")
        print(number)

        game(number, chances)


    elif user_input == 2:
        number = random.randint(0, 200)
        print(number)

        game(number, chances)



    while True:
        play_again = input("Do you wan to play again? (y/n): ")
        if play_again == "n":
            print("Thanks for playong.")
            exit()
        elif play_again == "y":
            print("Starting a new game.")
            print("................................................................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")