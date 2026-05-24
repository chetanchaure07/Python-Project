#  Simple Calculator with History
#  Author: Chetan Chaure
    # Features:
    # - Addition
    # - Subtraction
    # - Multiplication
    # - Division
    # - Power
    # - Save Calculation History
    # - Clear History
FILENAME = "cal_history.txt"
def calculator():
    while True:
        try:
            print("1. Use Calculator")
            print("2. Show History")
            print("3. Clear History")
            print("4. Exit")

            option = int(input("Enter Your Choice :"))

            if option == 1:
                a = float(input("Enter First Number :"))
                b = float(input("Enter Second number :"))
                print("Now Enter Operation\nFor Addition '+'\nFor Subtraction '-'\nFor Multiply '*'\nFor Division '/'\nFor Power '^'")
                o = input("Enter operation :")
                print()

                match o:
                    case '+':
                        result = a + b
                    case '-':
                        result = a - b
                    case '*':
                        result = a * b
                    case '/':
                        if b == 0:
                            print("Cannot Divide by Zero")
                            continue
                        result = a / b
                    case '^':
                        result = a ** b
                    case _:
                        print("Invalid Operation")
                        continue

                with open(FILENAME, "a") as file:
                    file.write(f"{a} {o} {b} = {result}\n")
                print(f"{a} {o} {b} = {result}\n")
            
            elif option == 2:
                try:
                    with open(FILENAME, "r") as file:
                        cal_history = file.read()
                    print(cal_history)
                except FileNotFoundError:
                    print("File Not Found")
                
            elif option == 3:
                try:
                    with open(FILENAME, "w") as file:
                        file.write("")
                        print("History Cleared")
                    
                except FileNotFoundError:
                    print("File Not Found")
            
            elif option == 4:
                print("Exiting...")
                break

            else:
                print("Invalid Option")
                continue

        except ValueError:
            print("Enter valid Value of 'a' and 'b'.")
calculator()