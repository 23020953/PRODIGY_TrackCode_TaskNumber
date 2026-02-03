import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                
                if isinstance(data, list):
                    return data
                
                return []
        except (json.JSONDecodeError, OSError):
            
            return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print(" Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print(" No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to edit: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= index < len(contacts):
        contacts[index]["name"] = input("New name: ")
        contacts[index]["phone"] = input("New phone: ")
        contacts[index]["email"] = input("New email: ")

        save_contacts(contacts)
        print(" Contact updated successfully!")
    else:
        print(" Invalid contact number")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to delete: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number")


def main():
    contacts = load_contacts()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print(" Invalid choice")

if __name__ == "__main__":
    main()
