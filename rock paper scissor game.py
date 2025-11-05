import random

choices = {1: "Rock", 2 : "Paper", 3: "Scissor"}


while True:
    while True:
        try:
            user_input = int(input("Please choose an option. \n1. Rock \n2. Paper\n3. Scissor: "))
            if user_input in [1,2,3]:
                break
            else:
                print("Invalid number. Please input 1, 2 or 3")
                continue
        except ValueError:
            print("Invalid input. Please input a whole number between 1 and 3")

    computer = random.randint(1, 3)
    print(f"You chose {choices[user_input]} and computer chose {choices[computer]}")


    if user_input == computer:
        print("It's a draw")
    elif user_input == 1 and computer == 3:
        print("You won.")
    elif user_input == 3 and computer == 1:
        print("You lose.")
    elif computer > user_input:
        print("You lose.")
    elif user_input > computer:
        print("You won.")

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