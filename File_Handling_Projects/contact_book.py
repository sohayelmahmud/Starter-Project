





def get_user_choice():
    """
    Displays the menu options and repeatedly prompts the user for a valid
    integer choice (1-6) until a correct value is entered.
    """
    while True:
        try:
            print("\n" + "="*34)
            print("WELCOME TO THE CONTACTBOOK MANEGER")
            print("="*34)

            choice = int(input("\n1. View All Contacts \n" \
                               "2. Add New Contact \n" \
                               "3. Search Contact \n" \
                               "4. Edit Contact \n" \
                               "5. Delete Contact \n" \
                               "6. Exit"
                               "..................... \n" \
                               "Enter your Choice (1-6): "))

            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")
