import random

print("Welcome to Number Guessing Game")


user_input = int(input("Do you want to set the range of number or let me set it for you? \n1. I want to set \n2. You can set: "))

chances = 5

if user_input == 1:
    minimum = int(input("Set the minimum range of number: "))
    maximum = int(input("Set the maximum range of number: "))
    number = random.randint(minimum, maximum)
    print(number)

    while chances > 0:
        guess = int(input("Guess the number: "))
        if number == guess:
            print("Congratulation! You guessed it right.")
            break

        else:
            if chances != 1:
                if (guess - 20) > number:
                    print("The guess is too high!")
                elif guess > number:
                    print("The guess is high!")
                elif (guess + 20) < number:
                    print("The guess is too low!")
                elif guess < number:
                    print("The guess is low!")

                print(f"You have {chances-1} chances left. Try again.")
            else:
                print("You lost! Better luck next time")
            chances -= 1
            continue


if user_input == 2:
    number = random.randint(0, 200)
    print(number)

    while chances > 0:
        guess = int(input("Guess the number: "))
        if number == guess:
            print("Congratulation! You guessed it right.")
            break

        else:
            if chances != 1:
                if (guess - 20) > number:
                    print("The guess is too high!")
                elif guess > number:
                    print("The guess is high!")
                elif (guess + 20) < number:
                    print("The guess is too low!")
                elif guess < number:
                    print("The guess is low!")

                print(f"You have {chances-1} chances left. Try again.")
            else:
                print("You lost! Better luck next time")
            chances -= 1
            continue
