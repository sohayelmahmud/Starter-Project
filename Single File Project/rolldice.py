import random

while True:
    print(random.randint(1, 6))

    while True:
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks for playing. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting a new game.")
            print("......................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")