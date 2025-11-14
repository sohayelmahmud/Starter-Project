while True:
    user_input = input("Enter your text: \n").strip()
    word_list = user_input.split()

    if not word_list:
        word_count = 0
    else:
        word_count = len(word_list)


    letter_count = len(user_input.replace(' ', ''))

    print(f"\nThis text contains {word_count} words.")
    print(f"This text contains {letter_count} letters (excluding spaces).")


    while True:
        play_again = input("Do you want to check another text? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting again.")
            print("................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")