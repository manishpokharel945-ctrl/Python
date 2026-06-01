contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def view_contacts():
    if len(contacts) == 0:
        print("\nNo contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("\n--- Contact Found ---")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you for using Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")


main()