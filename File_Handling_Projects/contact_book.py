import os
import json
folder_path = "File_Handling_Projects"
file_path = f"{folder_path}/contacts.json"

def view_contact():
    if not os.path.exists(file_path):
        print("Your Contact is empty.")
        input("Press Enter to return to the Main Menu...")
        return

    try:
        with open (file_path, "r") as file:
            contacts = json.load(file)

            if not contacts:
                print("Your Contact is empty.")
                input("Press Enter to return to the Main Menu...")
                return

            contacts.sort(key=lambda contact: contact['name'])

            print("\n=========================================================")
            print(f"| {'Name':<30} | {'Phone Number':<20} |")
            print("=========================================================")

            for index, contact in enumerate(contacts, 1):
                print(f"| {contact['name']:<30} | {contact['phone']:<20} |")
            print("---------------------------------------------------------")
        input("\nPress Enter to return to the Main Menu...")

    except json.JSONDecodeError:
        print(f"\nError: The contact file is corrupted or contains invalid JSON data.")
    except Exception as e:
        print(f"\nAn error occurred while reading the contact file: {e}")


def load_contact():
    if not os.path.exists(file_path) or os.path.getsize(file_path)==0:
        return []

    try:
        with open (file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\nWarning: Contact file is corrupted. Starting with a fresh list.")
        return []
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []


def save_contact(contact_list):
    try:
        os.makedirs(folder_path, exist_ok=True)
        with open (file_path, "w") as file:
            json.dump(contact_list, file, indent=4)
    except Exception as e:
        print(f"\nError saving contacts: {e}")


def add_contact():
    print("\nNew Contact Details:")
    name = input("Enter Name: ").strip().title()
    phone = input("Enter Number: ").strip()

    if not name or not phone:
        print("Name and Phone number cannot be empty. Contact addition cancelled.")
        return

    contacts = load_contact()
    new_contact = {
        "name": name,
        "phone": phone
    }
    contacts.append(new_contact)
    save_contact(contacts)

    print(f"\nContact '{name}' added successfully.")


def search_contact():
    contacts = load_contact()

    if not contacts:
        print("\nContact book is empty. Nothing to search.")
        input("Press Enter to return to the Main Menu...")
        return

    keyword = input("\nEnter Name or Phone Number (partial match allowed) to search: ").lower().strip()
    if not keyword:
        print("Search term cannot be empty. Search cancelled.")
        return

    match_contact = []

    for contact in contacts:
        name = contact.get('name', '').lower()
        phone = contact.get('phone', '')

    if keyword in name or keyword in phone:
        match_contact.append(contact)


    print("\nSEARCH RESULTS:")

    if match_contact:
        match_contact.sort(key=lambda contact: contact['name'])

        print("\n=========================================================")
        print(f"| {'Name':<30} | {'Phone Number':<20} |")
        print("=========================================================")
        for contact in match_contact:
            print(f"| {contact['name']:<30} | {contact['phone']:<20} |")

        print("---------------------------------------------------------")
    else:
        print(f"No contacts found matching '{keyword}'.")

    input("\nPress Enter to return to the Main Menu...")
#  not working..... do ot later


def edit_contact():
    pass



def del_contact():
    pass





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
                               "6. Exit \n"
                               "........................ \n" \
                               "Enter your Choice (1-6): "))

            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        choice = get_user_choice()

        if choice == 1:
            view_contact()
        elif choice == 2:
            add_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            del_contact()
        else:
            print("Exiting application.")
            break

if __name__ == "__main__":
    main()
