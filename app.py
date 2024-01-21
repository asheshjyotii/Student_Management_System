student_details = {}

while exit != 1:
    print("Student Management System")
    print("Enter '1' to Add a new student")
    print("Enter '2' to Edit details of a student")
    print("Enter '3' to Delete details of a student")
    print("Enter '4' to Display all student's records")
    print("Enter '5' to Display a specific student's records")
    print("Enter '6' to Exit the System")

    choice = int(input("Enter your choice: "))

    if choice == 1 :
        print("Enter the new Student Details as follows: ")
        new_student_name = input("Enter the Student Name: ")
        if new_student_name in student_details:
            print("Student already present Choose again")
            continue
        new_student_age = input("Enter the Student Age: ")
        new_student_grade = input("Enter the Student Grade: ")

        new_entry = {new_student_name:{'age': new_student_age, 'grade': new_student_grade}}
        student_details.update(new_entry)
    elif choice == 2:
        edit_details_of = input("Enter the name of the student to edit details: ")
        if edit_details_of not in student_details:
            print("Student not present Choose again")
            continue
        to_edit = int(input("Enter 1 to edit the Age, 2 to edit the Grade "))
        if to_edit == 1:
            new_age = int(input(f"Enter the new Age of {edit_details_of}: "))
            student_details[edit_details_of]["age"]= new_age
            print(f"Updated {edit_details_of}'s Age to : {student_details[edit_details_of]['age']}")
        else :
            new_grade = int(input(f"Enter the new Grade of {edit_details_of}: "))
            student_details[edit_details_of]["grade"]= new_grade
            print(f"Updated {edit_details_of}'s Grade to : {student_details[edit_details_of]['grade']}")
    elif choice == 3:
        name_to_delete = input("Enter the student's name to delete his/her record :")
        if name_to_delete not in student_details:
            print("Student not present Choose again")
            continue
        del student_details[name_to_delete]
    elif choice== 4:
        print("---------------------------------")
        print("|---Name---|----Age---|--grade--|")
        print("---------------------------------")
        for name,details in student_details.items():
            print("|"+name.center(10,' '),end='')
            print("|"+details['age'].center(10,' '),end='')
            print("|"+details['grade'].center(9,' ')+"|")
            print("---------------------------------")

    elif choice==5:
        specific_student_name = input("Enter the Name of the student to get details: ")
        if specific_student_name not in student_details:
            print("Student not present Choose again")
            continue

        print("---------------------------------")
        print("|---Name---|----Age---|--grade--|")
        print("---------------------------------")
        print("|"+specific_student_name.center(10,' '),end='')
        print("|" + student_details[specific_student_name]['age'].center(10, ' '), end='')
        print("|" + student_details[specific_student_name]['grade'].center(9, ' ') + "|")
        print("---------------------------------")