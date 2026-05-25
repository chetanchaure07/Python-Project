'''# KBC Quiz Game in Python

A simple console-based Kaun Banega Crorepati (KBC) quiz game built using Python.

## Features
- 10 Quiz Questions
- Prize Money System
- Exception Handling
- User Input Validation

## Run

python kbc_game.py
'''
def kbc():
    questions = [
        ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
        ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
        ["Who wrote 'Hamlet'?", "Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen", 2],
        ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
        ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
        ["What is 5 + 7?", "10", "11", "12", "13", 3],
        ["Which country is famous for the pyramids?", "India", "Mexico", "Egypt", "China", 3],
        ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 3],
        ["What is the boiling point of water at sea level?", "90°C", "100°C", "110°C", "120°C", 2],
        ["Which language is primarily used for web development?", "Python", "HTML", "C++", "Java", 2]
    ]
    price = [1000, 2000, 3000, 5000, 7500, 10000, 15000, 20000, 35000, 50000]

    try:
        i = 0
        for question in questions:
            print(question[0])

            print("Your Option Are...")
            print(f"1. {question[1]}\n2. {question[2]}\n3. {question[3]}\n4. {question[4]}")
            option = int(input("Choose Option :"))

            if option == question[5]:
                print("Correct Answer")
                print(f"You Won : ${price[i]}")
            
            else:
                print("You Lose")
                print(f"Correct Answer Was : {question[question[5]]}")
                print(f"You Won : ${price[i-1] if i > 0 else 0}")
                break
            i += 1
    except Exception as error:
        print(error)
kbc()