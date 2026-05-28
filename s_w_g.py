'''# Snake Water Gun Game

A simple Snake-Water-Gun game made using Python.

## Features
- Random computer moves
- User input validation
- Exception handling
- Infinite gameplay loop

## Technologies Used
- Python
- random module

## How to Run

```bash
python game.py'''
import random
while True:
    try:
        choices = ["Snake", "Water", "Gun"]
        print("Snake : 1\nWater : 2\nGun : 3")
        user_choice = choices[int(input("Enter Your Choice (eg. 1, 2, 3): ")) - 1]
        com_choice = random.choice(choices)
        
        if user_choice in choices:
            if (user_choice == "Snake" and com_choice == "Water") or (user_choice == "Water" and com_choice == "Gun") or (user_choice == "Gun" and com_choice == "Snake"):
                print(f"User Choice is: {user_choice}")
                print(f"Computer Choice is: {com_choice}")
                print()
                print("User Win!")
                print()
            elif (user_choice == "Snake" and com_choice == "Snake") or (user_choice == "Water" and com_choice == "Water") or (user_choice == "Gun" and com_choice == "Gun"):
                print(f"User Choice is: {user_choice}")
                print(f"Computer Choice is: {com_choice}")
                print()
                print("Match Draw!")
                print()
            else:
                print(f"User Choice is: {user_choice}")
                print(f"Computer Choice is: {com_choice}")
                print()
                print("Computer Win!")
                print()
        else:
            print("Valid Input is: 1, 2, 3")
    except ValueError:
        print("Enter Valid Input (eg. 1, 2, 3)")
    except IndexError:
        print("Enter 1, 2, 3 only")
        
