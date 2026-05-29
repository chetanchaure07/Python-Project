'''# Task Manager

A simple command-line Task Manager built with Python.

## Features

- Add Tasks
- View Tasks
- Mark Tasks as Completed
- Delete Tasks
- Desktop Notifications

## Requirements

pip install plyer

## Run

python main.py'''

from datetime import datetime 
from plyer import notification
import os

FILENAME = "TO_DO.txt"

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )
def add_task():
    try:
        task = input("Enter Task: ")
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")
        with open(FILENAME, "a") as file:
            file.write(f"Date : {date} | Time : {time} | Task : {task} | Status : Pending\n")
        print(f"Your {task} Task Is Added.")
        send_notification(title="Task Added", message=f"Your {task} Task Is Added.")
    except Exception as e:
        print(f"Error: {e}")
def show_all_task():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

            if lines:
                print("Here Is Your Task>>\n")
                for i, line in enumerate(lines, start=1):
                    print(i, line)
            else:
                print("No History Found")
    except FileNotFoundError:
        print("File Not Found.")
def change_status():
    try:
        show_all_task()
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        
        change_status_line = int(input("Enter Task Number Which You Completed: "))

        if change_status_line < 1 or change_status_line > len(lines):
            print("Invalid Selection.")
            return

        for i, line in enumerate(lines, start=1):
            if i == change_status_line:
                part = line.strip().split("|")
                part[3] = " Status : Completed"
                lines[i - 1] = "|".join(part) + "\n"
                break
        
        with open(FILENAME, "w") as file:
            file.writelines(lines)
        
        send_notification(title="Completed Task", message="Keep Growing, Keep Moving Forward Your Goal.")
        
    except Exception as error:
        print(f"Error: {error}")

def delete_task():
    try:
        show_all_task()
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        
        del_line_int = int(input("Enter Line No which You Want To Delete: "))

        if del_line_int < 1 or del_line_int > len(lines):
            print("Enter Valid Input")
            return

        with open(FILENAME, "w") as file:
            for i, line in enumerate(lines, start=1):
                if i != del_line_int:
                    file.write(line)

        print("Task deleted successfully.")

        send_notification(title="Delete Task", message="Task Deleted Successfully.")
    except Exception as error:
        print(f"Error: {error}")
    
while True:
    try:
        print("Task Manager>>")
        print("1. Add Task")
        print("2. Show All Task")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        if not os.path.exists(FILENAME):
            with open(FILENAME, "w") as file:
                file.write("")

        choice = int(input("Enter Task Number: "))

        if choice == 1:
            add_task()
        
        elif choice == 2:
            show_all_task()
        
        elif choice == 3:
            change_status()

        elif choice == 4:
            delete_task()
        
        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Enter Valid Value.")
            continue

    except ValueError:
        print("Enter Valid Value.")
