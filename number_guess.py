# This is number guessing game
import random

def number_guessing_game():
    secrete_number = random.randint(1, 100)

    count = 0
    while True:
        try:
            user_guess = int(input("Guess The Number: "))

            count += 1
            if secrete_number == user_guess:
                print("You Won...")
                print(f"You Got {count} Chance To Win.\n")
                break

            elif secrete_number > user_guess:
                print("Too Low, Guess Higher Value")

            elif secrete_number < user_guess:
                print("Too High, Guess Lower Value")

        except ValueError:
            print("Error: Enter only valid integer value")
        except Exception as error:
            print(f"Error: {error}")

    choice = input("Want To Play Again Y/N: ").lower().strip()
    if choice == "y":
        number_guessing_game()

number_guessing_game()