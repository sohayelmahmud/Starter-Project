while True:
    while True:
        try:
            user_input = int(input("Enter the number of terms for the Fibonacci series: "))

            if user_input > 0:
                break
            else:
                print("Please enter a positive integer (1 or more).")
                continue

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    a = 0
    b = 1
    count = 0

    print(f"\nThe first {user_input} terms of the Fibonacci series:")

    if user_input == 1:
        print(a)

    elif user_input >= 2:
        print(a, end=" ")
        print(b, end=" ")
        count = 2

        while count < user_input:
            next_term = a + b

            print(next_term, end=" ")

            a = b
            b = next_term

            count += 1

        print()


    while True:
        play_again = input("Do you want to print again? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting again.")
            print("................................................................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")
