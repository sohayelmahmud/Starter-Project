# def reverse_string(text):
#     return text[::-1]


while True:
    user_input = input("Enter the text you want to reverse: ").strip()

    if not user_input:
        print("Input cannot be empty. Please enter some text.")
        continue

    reversed_text = user_input[::-1]

    print(f"\nOriginal Text: {user_input}")
    print(f"Reversed Text: {reversed_text}")

    while True:
        play_again = input("\nDo you want to reverse another text? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting again.")
            print("................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")