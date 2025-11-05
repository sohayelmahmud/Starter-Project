while True:
    while True:
        try:
            user_input = int(input("Please enter the number: "))
            break
        except ValueError:
            print("Please enter a valid number")


    for i in range (11):
        print(f"{i} * {user_input} = {i*user_input}")

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