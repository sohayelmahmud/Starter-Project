while True:
    while True:
        try:
            user_input = abs(int(input("Input a digit: ")))
            break

        except ValueError:
            print("Invalid input. Please input a whole number.")

    sum = 0

    while user_input > 0:
            digit = user_input % 10
            sum += digit
            user_input //= 10

    print(f"Sum of this digit: {sum}")


    while True:
        play_again = input("Do you want to sum again? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting again.")
            print("................................................................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")
