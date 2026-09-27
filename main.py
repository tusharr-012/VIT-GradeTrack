from subject import add_subject, view_subjects, enter_marks, attendance_check, search_subject, delete_subject, subjects
from calculator import marks_analysis



def show_menu():
    print()
    print("================================")
    print("          VIT GRADETRACK")
    print("================================")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Enter Marks")
    print("4. Attendance Check")
    print("5. Marks Analysis")
    print("6. Search Subject")
    print("7. Delete Subject")
    print("8. Exit")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_subject()
        

    elif choice == "2":
        view_subjects()

    elif choice == "3":
        enter_marks()
        

    elif choice == "4":
         attendance_check()

    elif choice == "5":
         marks_analysis(subjects)

    elif choice == "6":
           search_subject()

    elif choice == "7":
         delete_subject()
        

    elif choice == "8":
        print("Thank you for using VIT GradeTrack!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 8.")