import os
import datetime

folder_path = "File_Handling_Projects"
file_path = f"{folder_path}/diary.txt"


def add_entry():
    entry = input("Write your diary entry: ")
    timestamp = datetime.datetime.now().strftime("[%b %-d, %Y -- %-I:%M %p]")
    entry_line = f"{entry} == {timestamp}\n"

    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder {folder_path}: {e}")
        return

    with open (file_path, "a") as file:
        file.write(entry_line)
    print("Entry added successfully.")


def view_entry():
    print("\nALL DIARY ENTRIES:")
    print("====================================")
    if not os.path.exists(file_path):
        print("Your Diary is empty. No entries found.")
        input("Press Enter to return to the Main Menu...")
        return

    try:
        with open (file_path, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Your Diary is empty. No entries found.")
                input("Press Enter to return to the Main Menu...")
                return

            for count, line in enumerate(lines, 1):
                print(f"{count}. {line.strip()}")
        input("Press Enter to return to the Main Menu...")

    except Exception as e:
        print(f"An error occurd while reading the task file: {e}")


def search_entry():
    if not os.path.exists(file_path):
        print("Diary file not found. Nothing to search.")
        return

    keyword = input("Enter keyword or date (e.g., 2025-11-24) to search: ").lower()
    match_entry = []

    try:
        with open (file_path, "r") as file:
            for line in file:
                if keyword in line.lower():
                    match_entry.append(line.strip())

        print("\nSearch Results")
        print("="*20)

        if match_entry:
            for entry in match_entry:
                print(entry)
        else:
            print(f"No entries found containing '{keyword}'.")
            input("\nPress Enter to return to the Main Menu...")
        input("Press Enter to return to the Main Menu...")

    except Exception as e:
        print(f"An error occurd during search: {e}")


def del_entry():
    try:
        if not os.path.exists(file_path):
            print("Diary file not found. Nothing to delete.")
            return

        with open (file_path, "r") as file:
            lines = file.readlines()

        if not lines:
            print("The diary is empty. Nothing to delete.")
            return

        print("ENTRIES TO DELETE FROM:")
        print(".......................")
        for count, line in enumerate(lines, 1):
            print(f"{count}. {line.strip()}")

        while True:
            try:
                choice = int(input("Which entry number do you want to delete? (Enter 0 to cancel): "))

                if choice == 0:
                    print("Deletion cancelled.")
                    return
                if 1 <= choice <= len(lines):
                    break
                else:
                    print(f"Invalid entry number. Please enter a number between 1 and {len(lines)} or '0' to cancel.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        new_lines = [line for index, line in enumerate(lines, 1) if index != choice]

        with open(file_path, "w") as file:
            file.writelines(new_lines)

        print(f"Entry [{choice}] deleted successfully!")
        view_entry()

    except ValueError:
        pass


def get_user_choice():
    """
    Displays the menu options and repeatedly prompts the user for a valid
    integer choice (1-4) until a correct value is entered.
    """
    while True:
        try:
            print("\n" + "="*34)
            print("WELCOME TO THE SIMPLE DIARY/NOTEBOOK")
            print("="*34)

            choice = int(input("\n1. View All Entries \n" \
                               "2. Add New Entry \n" \
                               "3. Search Entries \n" \
                               "4. Delete Entry \n" \
                               "5. Exit \n"
                               "..................... \n" \
                               "Enter your Choice (1-5): "))

            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        choice = get_user_choice()

        if choice == 1:
            view_entry()
        elif choice == 2:
            add_entry()
        elif choice == 3:
            search_entry()
        elif choice == 4:
            del_entry()
        else:
            print("Exiting application.")
            break

if __name__ == "__main__":
    main()