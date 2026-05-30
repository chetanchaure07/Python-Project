FILENAME = "Student_File.txt"
while True:
    try:
        print("Student Manger.")
        print("1. Add Studnet")
        print("2. Search Student")
        print("3. Update Student Marks")
        print("4. Delete Student Detail")
        print("5. View All Student Info")
        print("6. Exit")

        with open(FILENAME, "a") as file:
            file.write("")

        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            student_roll_no = int(input("Enter Student Roll No: "))
            student_name = input("Enter Student Name: ")
            student_marks = int(input("Enter Student Marks: "))
            with open(FILENAME, "a") as file:
                file.write(f"Roll No : {student_roll_no}, Name : {student_name}, Marks : {student_marks}\n")
            print(f"{student_name}'s Info Saved.")
        elif choice == 2:
            search_student = int(input("Enter Student ID No: "))
            with open(FILENAME, "r") as file:
                lines = file.readlines()

                found = False
                for line in lines:
                    roll_no = int(line.split(",")[0].split(":")[1].strip())

                    if search_student == roll_no:
                        print()
                        print(line)
                        found = True
                        break
                if not found:
                    print("Student Not Found")
        elif choice == 3:
            update_student = int(input("Enter Student ID No: "))
            with open(FILENAME, "r") as file:
                lines = file.readlines()

                found = False
                for i in range(len(lines)):
                    roll_no = int(lines[i].split(",")[0].split(":")[1].strip())

                    if update_student == roll_no:
                        updated_marks = int(input("Enter Your Updated Marks: "))
                        name = lines[i].split(",")[1].split(":")[1].strip()
                        lines[i] = f"Roll No : {roll_no}, Name : {name}, Marks : {updated_marks}\n"
                        found = True
                        break
                if not found:
                    print("Student Not Found")
                else:
                    with open(FILENAME, "w") as file:
                        file.writelines(lines)
                    print("Marks Updated.")
        elif choice == 4:
            del_student = int(input("Enter Student ID No: "))
            with open(FILENAME, "r") as file:
                lines = file.readlines()

                found = False
                for i in range(len(lines)):
                    roll_no = int(lines[i].split(",")[0].split(":")[1].strip())

                    if del_student == roll_no:
                        del lines[i]
                        found = True
                        break
                if not found:
                    print("Student Not Found")
                else:
                    with open(FILENAME, "w") as file:
                        file.writelines(lines)
                    print("Student Detail Deleted.")
        elif choice == 5:
            with open(FILENAME, "r") as file:
                lines = file.readlines()

                if lines:
                    for line in lines:
                        print(line)
                else:
                    print("No Student Record.")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Enter Valid Input")
        
    except Exception as error:
        print(f"Error: {error}")
    
