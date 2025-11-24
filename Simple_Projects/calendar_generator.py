import calendar
import sys


def get_input():
    while True:
        try:
            year = int(input("Enter the Year (e.g., 2025): "))
            month = int(input("Enter the Month (1-12): "))

            if 1 <=month <= 12 and year >0:
                return year, month
            else:
                print("Invalid input! Please ensure the month is 1-12 and the year is positive.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for year and month.")


def print_calendar(year, month):
    print("\n ---Generated Calendar---")
    print(calendar.month(year, month))
    print("...........................")


import sys # exit() ব্যবহারের জন্য sys মডিউল ইম্পোর্ট করা

def play_again():
    while True:
        play_again = input("Do you want to print another calendar? (y/n): ").lower().strip()

        if play_again == "n":
            print("Thanks. Goodbye!")
            sys.exit()

        elif play_again == "y":
            print("\nStarting again...")
            return True

        else:
            print("Invalid Input. please enter 'y' or 'n'.")


def main():
    while True:
        year, month = get_input()
        print_calendar(year, month)
        play_again()


if __name__ == "__main__":
    main()
