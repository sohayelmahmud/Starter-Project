# will fix bug for valuerror,

import random

def game(number, chances = 5):
        while chances > 0:
            guess = int(input("Guess the number: "))
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
    user_input = int(input("Do you want to set the range of number or let me set it for you? \n1. I want to set \n2. You can set: "))

    chances = 5
    number = 0

    if user_input == 1:
        minimum = int(input("Set the minimum range of number: "))
        maximum = int(input("Set the maximum range of number: "))
        number = random.randint(minimum, maximum)
        print(number)

        game(number, chances)


    elif user_input == 2:
        number = random.randint(0, 200)
        print(number)

        game(number, chances)


    play_again = input("Do you wan to play again? (y/n): ")

    if play_again == "n":
        print("Thanks for playong.")
        break
    elif play_again == "y":
        print("Starting a new game.")
        print("................................................................")
        continue
    else:
        print("Invalid Input. Assuming you meant 'n'. Exiting.")
        break