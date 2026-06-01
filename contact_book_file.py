'''
# Contact Book Management System

A simple Python-based Contact Book that uses file handling to store and manage contact information.

## Features

* Add Contact
* Search Contact
* Update Contact
* Delete Contact
* View All Contacts
* Persistent data storage using a text file

## Technologies Used

* Python 3
* File Handling
* Exception Handling

## Run the Project

```bash
python contact_book.py
```

## Project Structure

```text
Contact-Book/
├── contact_book.py
├── Contact_Book.txt
└── README.md
```

## Author

Chetan Chaure
'''

FILENAME = "Contact_Book.txt"

def add_contact():
    try:
        person_name = input("Enter Person Name: ").title().strip()
        person_phone = input("Enter Person Phone No: ").strip()
        person_email = input("Enter Person Email: ").strip()

        with open(FILENAME, "a") as file:
            file.write(
                f"Name : {person_name} | Phone No : {person_phone} | Email : {person_email}\n"
            )

        print(f"{person_name}'s information saved successfully.")

    except Exception as error:
        print(f"Error: {error}")


def search_contact():
    try:
        person_name = input("Enter Person Name: ").title().strip()

        with open(FILENAME, "r") as file:
            contacts = file.readlines()

        found = False

        for line in contacts:
            name = line.split("|")[0].split(":")[1].strip()

            if name == person_name:
                print("\nContact Found:")
                print(line)
                found = True
                break

        if not found:
            print(f"{person_name}'s information not found.")

    except FileNotFoundError:
        print("No contacts found. Contact file does not exist.")
    except Exception as error:
        print(f"Error: {error}")


def delete_contact():
    try:
        person_name = input("Enter Person Name: ").title().strip()

        with open(FILENAME, "r") as file:
            contacts = file.readlines()

        updated_contacts = []
        found = False

        for line in contacts:
            name = line.split("|")[0].split(":")[1].strip()

            if name != person_name:
                updated_contacts.append(line)
            else:
                found = True

        with open(FILENAME, "w") as file:
            file.writelines(updated_contacts)

        if found:
            print(f"{person_name}'s information deleted successfully.")
        else:
            print(f"{person_name}'s information not found.")

    except FileNotFoundError:
        print("No contacts found. Contact file does not exist.")
    except Exception as error:
        print(f"Error: {error}")


def update_contact():
    try:
        person_name = input("Enter Person Name: ").title().strip()

        with open(FILENAME, "r") as file:
            contacts = file.readlines()

        updated_contacts = []
        found = False

        for line in contacts:
            name = line.split("|")[0].split(":")[1].strip()

            if name == person_name:
                new_phone = input("Enter New Phone No: ").strip()

                update_email = input(
                    "Do You Want To Update Email? (Y/N): "
                ).strip().upper()

                old_email = line.split("|")[2].split(":")[1].strip()

                if update_email == "Y":
                    new_email = input("Enter New Email: ").strip()
                else:
                    new_email = old_email

                updated_line = (
                    f"Name : {person_name} | "
                    f"Phone No : {new_phone} | "
                    f"Email : {new_email}\n"
                )

                updated_contacts.append(updated_line)
                found = True

            else:
                updated_contacts.append(line)

        with open(FILENAME, "w") as file:
            file.writelines(updated_contacts)

        if found:
            print(f"{person_name}'s information updated successfully.")
        else:
            print(f"{person_name}'s information not found.")

    except FileNotFoundError:
        print("No contacts found. Contact file does not exist.")
    except Exception as error:
        print(f"Error: {error}")


def view_all_contacts():
    try:
        with open(FILENAME, "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("No contacts available.")
            return

        print("\n===== All Contacts =====")

        for contact in contacts:
            print(contact.strip())

    except FileNotFoundError:
        print("No contacts found. Contact file does not exist.")
    except Exception as error:
        print(f"Error: {error}")


def contact_book():
    while True:
        try:
            print("\n===== Contact Book Menu =====")
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. Delete Contact")
            print("4. Update Contact")
            print("5. View All Contacts")
            print("6. Exit")

            choice = input("Enter Your Choice: ").strip()

            if choice == "1":
                add_contact()

            elif choice == "2":
                search_contact()

            elif choice == "3":
                delete_contact()

            elif choice == "4":
                update_contact()

            elif choice == "5":
                view_all_contacts()

            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    contact_book()