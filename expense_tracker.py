'''# Expense Tracker

A simple Python expense tracker using file handling.

## Features
- Add Expense
- View Expense History
- Calculate Total Expense

## Technologies Used
- Python
- File Handling

## How to Run

```bash
python expense_tracker.py
'''
import datetime
FILENAME = "Expense_History.txt"        
def expense_tracker():
    while True:
            try:
                print("\n1. Add Expense.")
                print("2. View Expense.")
                print("3. Total Expense.")
                print("4. Exit.")
                option = int(input("Enter Your Option :"))
                
                if option == 1:
                    
                    item = input("Enter Item Name :")
                    amt = float(input("Enter Amount :"))
                    date = input("Enter Date (eg. 11/06/2026) :")

                    datetime.datetime.strptime(date, "%d/%m/%Y")

                    with open(FILENAME, "a") as file:
                        file.write(f"Item Name : {item} | Amount : {amt} | Date : {date}\n")
                    print(f"Item Name : {item} | Amount : {amt} | Date : {date}\n")
                    print("Your Expense Saved.")

                elif option == 2:
                    try:
                        with open(FILENAME, "r") as file:
                            expense = file.read()
                            if expense:
                                print("Expense History :")
                                print(expense)
                            else:
                                print("No Expense History Found")
                    except FileNotFoundError:
                        print("File Not Found")
                    
                elif option == 3:
                    try:
                        total = 0.0
                        with open(FILENAME, "r") as file:
                            lines = file.readlines()
                            for line in lines:
                                sec_line = line.split("|")
                                amount = sec_line[1].split(":")
                                total += float(amount[1])
                                
                        print(f"Here Is Your Total Expense : {total}")
                    except Exception as error:
                        print(error)

                elif option == 4:
                    print("Exiting...")
                    break
                
                else:
                    print("Invalid Option")
                    continue

            except ValueError:
                print("Give The Valid Input.")
            except Exception as error:
                print(f"Error : {error}")

expense_tracker()