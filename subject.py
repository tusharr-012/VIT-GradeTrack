from validator import get_mark

subjects = []


def add_subject():
    name = input("Enter subject name: ")
    code = input("Enter subject code: ")

    subject = {
        "name": name,
        "code": code
    }

    subjects.append(subject)

    print("Subject added successfully!")


def view_subjects():
    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    print()
    print("--------- SUBJECTS ---------")

    for subject in subjects:
        print("Subject:", subject["name"])
        print("Code:", subject["code"])

        if "cat1" in subject:
            print("CAT1:", subject["cat1"], "/ 50")
            print("CAT2:", subject["cat2"], "/ 50")
            print("TEE:", subject["tee"], "/ 100")
        else:
            print("Marks: Not entered yet")

        print("----------------------------")

def enter_marks():
    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    code = input("Enter subject code: ")

    for subject in subjects:
        if subject["code"].lower() == code.lower():

            cat1 = get_mark("Enter CAT1 marks (out of 50): ", 50)
            cat2 = get_mark("Enter CAT2 marks (out of 50): ", 50)
            tee = get_mark("Enter TEE marks (out of 100): ", 100)

            subject["cat1"] = cat1
            subject["cat2"] = cat2
            subject["tee"] = tee

            print("Marks added successfully!")
            return

    print("Subject not found.")


def attendance_check():
    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    code = input("Enter subject code: ")

    for subject in subjects:
        if subject["code"].lower() == code.lower():

            try:
                attendance = float(input("Enter attendance percentage: "))

                if attendance < 0 or attendance > 100:
                    print("Please enter attendance between 0 and 100.")
                    return

                print("Attendance:", attendance, "%")

                if attendance >= 75:
                    print("Attendance requirement met.")
                    print("Attendance marks: 5 / 5")
                else:
                    print("Attendance is below 75%.")
                    print("Full attendance marks are not applicable.")

                return

            except ValueError:
                print("Please enter a valid number.")

    print("Subject not found.")  

def search_subject():
    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    code = input("Enter subject code to search: ")

    for subject in subjects:
        if subject["code"].lower() == code.lower():
            print()
            print("Subject found!")
            print("Subject:", subject["name"])
            print("Code:", subject["code"])

            if "cat1" in subject:
                print("CAT1:", subject["cat1"], "/ 50")
                print("CAT2:", subject["cat2"], "/ 50")
                print("TEE:", subject["tee"], "/ 100")

            return

    print("Subject not found.") 

def delete_subject():
    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    code = input("Enter subject code to delete: ")

    for subject in subjects:
        if subject["code"].lower() == code.lower():
            subjects.remove(subject)
            print("Subject deleted successfully!")
            return

    print("Subject not found.")                          
         
         
