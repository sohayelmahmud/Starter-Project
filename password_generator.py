import random

latters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spc_char = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]

print("Welcome to our password generator.")
#main program start
while True:
    # take the length of pass from user
    try:
        length = int(input("Input the length of your password: "))
        if length <= 0:
            print("Password length must be a positive number")
            continue
    except ValueError:
        print("Invalid input. Please input a whole number")
        continue

    # take customaization from user
    num = str(input("Do you want to add numbers [y/n]? ")).lower().strip()
    spc = str(input("Do you want to add spacial cahracters [y/n]? ")).lower().strip()

    # initial list
    characters = list(latters)

    # customized list
    if num == "y":
        characters.extend(numbers)
    else:
        pass
    if spc == "y":
        characters.extend(spc_char)
    else:
        pass

    #chose chars and make pass
    password_chars = [random.choice(characters) for _ in range(length)]

    password = ''.join(password_chars)

    print(password)

    while True:
        play_again = input("Do you want to generate another password? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks.. Goodbye!")
            exit()
        elif play_again == "y":
            print("Creating a new password.")
            print("......................................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")
