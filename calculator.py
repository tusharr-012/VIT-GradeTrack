def calculate_total(subject):
    if "cat1" not in subject:
        return None

    total = subject["cat1"] + subject["cat2"] + subject["tee"]
    return total


def marks_analysis(subjects):
    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    totals = []

    print()
    print("--------- MARKS ANALYSIS ---------")

    for subject in subjects:
        total = calculate_total(subject)

        if total is not None:
            totals.append(total)

            print("Subject:", subject["name"])
            print("Code:", subject["code"])
            print("Total:", total, "/ 200")
            print("----------------------------")

    if len(totals) == 0:
        print("Marks have not been entered for any subject.")
        return

    average = sum(totals) / len(totals)

    print("Highest Total:", max(totals), "/ 200")
    print("Lowest Total:", min(totals), "/ 200")
    print("Average Total:", round(average, 2), "/ 200")