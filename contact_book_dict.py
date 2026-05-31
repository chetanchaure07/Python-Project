contacts = {}

def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"{name}'s information added successfully.")

def search_contact():
    name = input("Enter name to search: ").strip().title()
    if name in contacts:
        detail = contacts[name]
        print(f"Name: {name}, Phone: {detail['Phone']}, Email: {detail['Email']}")
    else:
        print(f"{name} info not found.")

def update_contact():
    name = input("Enter name to update: ").strip().title()
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        print("Contact updated successfully.")
    else:
        print(f"{name}'s information not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print(f"{name} not found.")

def view_all():
    if contacts:
        for name, detail in contacts.items():
            print(f"Name: {name}, Phone: {detail['Phone']}, Email: {detail['Email']}")
    else:
        print("No contacts available.")

def contact_book_with_dict():
    while True:
        try:
            print("Contact Book Manager")
            print("1. Add contact")
            print("2. Search contact")
            print("3. Update contact")
            print("4. Delete contact")
            print("5. View all contacts")
            print("6. Exit")

            choice = int(input("Choice Your Option: "))

            if choice == 1:
                add_contact()
            elif choice == 2:
                search_contact()
            elif choice == 3:
                update_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                view_all()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Enter Valid Input.")
        except ValueError:
            print("Enter Valid Integer Value")
        except Exception as error:
            print(f"Error: {error}")
contact_book_with_dict()