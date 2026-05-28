import random

items = ["Stone", "Paper", "Scissor"]

while True:
    try:
        print("\nStone   : 1")
        print("Paper   : 2")
        print("Scissor : 3")

        user_input = int(input("Enter Your Choice: "))

        # Validate input
        if user_input not in [1, 2, 3]:
            print("Enter only 1, 2, or 3")
            continue

        # Convert number to list index
        user_choice = items[user_input - 1]

        # Computer random choice
        com_choice = random.choice(items)

        print(f"\nYour Choice is: {user_choice}")
        print(f"Computer Choice is: {com_choice}\n")

        # Draw condition
        if user_choice == com_choice:
            print("Match Draw.\n")

        # Winning conditions
        elif (
            (user_choice == "Stone" and com_choice == "Scissor") or
            (user_choice == "Paper" and com_choice == "Stone") or
            (user_choice == "Scissor" and com_choice == "Paper")
        ):
            print("User WIN.\n")

        # Losing condition
        else:
            print("Computer WIN.\n")

    except ValueError:
        print("Enter Valid Integer Value.\n")