while True:
    while True:
        try:
            user_input = int(input("Please enter the digit: "))
            if user_input > 0:
                break
            else:
                print("Invalid digit. Please enter positive digit.")
        except ValueError:
            print("Invalid input. Please enter a valid digit.")

    factorial = 1
    num_for_print = user_input

    while user_input > 1:
        factorial *= user_input
        user_input -= 1

    print(f"The factorial of {num_for_print} is {factorial}")

    while True:
        again = input("Do you want to print again? (y/n)").lower().strip()

        if again == "y":
            print("starting again.")
            print(".........................")
            break
        elif again == "n":
            print("Thanks. Goodbye.")
            exit()
        else:
            print("Invalid input. Enter 'y' or 'n' ")