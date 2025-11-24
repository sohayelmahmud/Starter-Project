"""
To-Do List Manager

This script provides a simple command-line interface (CLI) for managing a to-do list.
Tasks are stored persistently in a text file ('task.txt') located inside a dedicated
folder ('File_Handling_Projects').

Features:
1. Display tasks with sequential numbering.
2. Add new tasks (with automatic folder creation if necessary).
3. Delete tasks by number.
4. Robust error handling for file operations and user input.

Dependencies:
- os (for file and directory management)

Usage:
Run the script and follow the menu prompts (1-4).
"""

import os

folder_path = "File_Handling_Projects"
file_path = f"{folder_path}/task.txt"


# show task
def show_task():
    print("\nCURRENT TO-DO LIST:")
    print("......................")

    if not os.path.exists(file_path):
        print("Your To-Do list is empty.")
        input("Press Enter to return to the Main Menu...")
        return

    try:
        with open (file_path, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Your To-Do list is empty.")
                input("Press Enter to return to the Main Menu...")
                return

            for count, line in enumerate(lines, 1):
                print(f"{count}. {line.strip()}")
        input("Press Enter to return to the Main Menu...")

    except Exception as e:
        print(f"An error occurd while reading the task file: {e}")


# add task
def add_task():
    task = input("Enter your task: ").capitalize()

    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {folder_path}: {e}")
        return

    with open (file_path, "a") as file:
        file.write(task+"\n")
    print("Task added.")


#delete task
def del_task():
    try:
        if not os.path.exists(file_path):
            print("The task file was not found. Please add a task first.")
            return

        with open (file_path, "r") as file:
            lines = file.readlines()

        if not lines:
            print("The to-do list is empty.")
            return

        print("Your Current To-do list:")
        for count, line in enumerate(lines, 1):
            print(f"{count}. {line.strip()}")

        choice = int(input("Which task do you want to delete? (Enter number) "))

        if 1 <= choice <= len(lines):
            new_lines = [line for index, line in enumerate(lines, 1) if index != choice]

            with open(file_path, "w") as file:
                file.writelines(new_lines)

            print("Task deleted.")
            show_task()
            input("Press Enter to return to the Main Menu...")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a number.")


# get input form user
def get_user_choice():
    """
    Displays the menu options and repeatedly prompts the user for a valid
    integer choice (1-4) until a correct value is entered.
    """
    while True:
        try:
            print("\n" + "="*34)
            print("WELCOME TO THE TO-DO LIST MANAGER")
            print("="*34)

            choice = int(input("\n1. Display Tasks \n" \
                               "2. Add New Task \n" \
                               "3. Delete Task \n" \
                               "4. Exit \n"
                               "..................... \n" \
                               "Enter your Choice (1-4): "))

            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")
#main func
def main():
    while True:
        choice = get_user_choice()

        if choice == 1:
            show_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            del_task()
        elif choice == 4:
            print("Exiting application.")
            break

main()