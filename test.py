import random

def game(number, chances = 5):
    """Handles the core guessing logic, chance counting, and hints."""
    while chances > 0:
        try:
            # --- 1. Guess Input Validation ---
            guess = int(input("Guess the number: "))
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")
            continue # ভুল ইনপুটের জন্য চান্স কমবে না

        if number == guess:
            print("🥳 Congratulation! You guessed it right.")
            return # জেতার পর ফাংশন থেকে বেরিয়ে যাও

        else:
            chances -= 1 # ভুল হলে চান্স কমবে

            if chances > 0:
                # --- Hints ---
                if (guess - 20) > number:
                    print("The guess is too high!")
                elif guess > number:
                    print("The guess is high!")
                elif (guess + 20) < number:
                    print("The guess is too low!")
                elif guess < number:
                    print("The guess is low!")

                print(f"You have {chances} chances left. Try again.")

    # যখন while লুপ শেষ হবে এবং return হয়নি (অর্থাৎ জেতা হয়নি)
    print(f"😔 You lost! The number was {number}. Better luck next time.")
    print("................................................................")


print("Welcome to Number Guessing Game")

# --- মূল লুপ: বারবার খেলার সুযোগ দেয় ---
while True:
    chances = 5
    number = 0

    # --- A. User Input Validation Loop (1 বা 2 নিশ্চিত করা) ---
    while True:
        try:
            user_input = int(input("Do you want to set the range of number or let me set it for you? \n1. I want to set \n2. You can set: "))

            if user_input in [1, 2]:
                break # সঠিক ইনপুট পেলে ভেতরের লুপ থেকে বেরিয়ে আসবে
            else:
                print("❌ Please enter 1 or 2 only.")
        except ValueError:
            print("❌ Invalid input. Please enter 1 or 2.")


    # --- B. Range Setting Logic ---
    if user_input == 1:
        # --- Minimum/Maximum Input Validation Loop ---
        while True:
            try:
                minimum = int(input("Set the minimum range of number: "))
                maximum = int(input("Set the maximum range of number: "))

                if minimum >= maximum:
                    print("❌ The minimum number must be strictly less than the maximum number.")
                    continue # ভুল হলে আবার রেঞ্জ চাইবে

                number = random.randint(minimum, maximum)
                print(f"Number set between {minimum} and {maximum}.")
                # print(number) # টেস্টিং শেষ হলে এই লাইনটি মুছে ফেলবেন!
                break # সঠিক রেঞ্জ সেট হলে লুপ থেকে বেরিয়ে আসবে
            except ValueError:
                print("❌ Invalid input! Please enter valid whole numbers for the range.")


    elif user_input == 2:
        number = random.randint(0, 200)
        print(number)
        print("Number set between 0 and 200.")
        # print(number) # টেস্টিং শেষ হলে এই লাইনটি মুছে ফেলবেন!


    # --- C. Game Start ---
    game(number, chances)


    # --- D. Play Again? Check ---
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower().strip()

        if play_again == "n":
            print("Thanks for playing. Goodbye!")
            exit() # পুরো প্রোগ্রাম বন্ধ করতে exit() ব্যবহার করা যায়
        elif play_again == "y":
            print("Starting a new game.")
            print("................................................................")
            break # ভেতরের লুপ বন্ধ করে বাইরের while True লুপের শুরুতে যাবে
        else:
            print("❌ Invalid Input. Please enter 'y' or 'n'.")