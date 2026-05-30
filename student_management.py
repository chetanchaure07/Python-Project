students = {}
while True:
    try:
        print("Student Management.")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. View All")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            student_roll_no = int(input("Enter Student Roll No (eg. 101): "))
            student_name = input("Enter Student Name: ")
            student_marks = int(input("Enter Student Marks: "))
            students[student_roll_no] = {"Name": student_name, "Marks": student_marks}
            print("Student added successfully.")
        elif choice == 2:
            search_student = int(input("Enter Student ID No: "))
            if search_student in students:
                print(f"Student Roll No: {search_student}, Name: {students[search_student]['Name']}, Marks: {students[search_student]['Marks']}")
            else:
                print("Student Not Found.")
        elif choice == 3:
            update_student = int(input("Enter Student ID No: "))
            if update_student in students:
                new_marks = int(input("Enter New Marks: "))
                students[update_student]["Marks"] = new_marks
                print("Student marks updated successfully.")
            else:
                print("Student Not Found.")
        elif choice == 4:
            delete_student = int(input("Enter Student ID No: "))
            if delete_student in students:
                del students[delete_student]
                print("Student deleted successfully.")
            else:
                print("Student Not Found.")
        elif choice == 5:
            if students:
                print("All Student Record")
                for roll_no, details in students.items():
                    print(f"Roll No : {roll_no}, Name : {details["Name"]}, Marks : {details["Marks"]}")
            else:
                print("No Student Record Available")
        elif choice == 6:
            print("Exiting...")
            break


    except ValueError:
        print("Invalid Input. Please enter a valid number.")   
    except Exception as error:
        print(f"Error: {error}")
    
