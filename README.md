# VIT GradeTrack

VIT GradeTrack is a simple Python project that helps a student keep track of subjects, marks and attendance.

It runs in the terminal and gives different options through a simple menu.

## Features

- Add subjects
- View subjects
- Enter CAT1, CAT2 and TEE marks
- Check attendance
- Calculate total marks
- See highest, lowest and average marks
- Search for a subject
- Delete a subject
- Handle wrong input

## Project Files

```text
VIT-GradeTrack/
│
├── main.py
├── subject.py
├── calculator.py
├── validator.py
├── README.md
├── statement.md
├── .gitignore
│
├── tests/
│   └── test_calculator.py
│
└── docs/
    └── design.md
```

### What each file does

**main.py**  
This is the main file of the project. It shows the menu and takes the user's choice.

**subject.py**  
This file contains the functions for adding, viewing, searching and deleting subjects. Marks and attendance are also handled here.

**calculator.py**  
This file is used for calculating total marks and showing basic marks analysis.

**validator.py**  
This file checks whether the marks entered by the user are valid.

**tests/test_calculator.py**  
This file contains the basic tests for the marks calculation.

## How to Run

### Requirements

You need Python 3 installed on your computer.

Pytest is only needed if you want to run the tests.

### Run the Program

1. Open the project folder in the terminal.
2. Run this command:

```bash
python main.py
```

3. The menu will appear.
4. Choose an option by entering its number.

## Menu

```text
1. Add Subject
2. View Subjects
3. Enter Marks
4. Attendance Check
5. Marks Analysis
6. Search Subject
7. Delete Subject
8. Exit
```

## Marks

For each subject, the program can take:

- CAT1 marks out of 50
- CAT2 marks out of 50
- TEE marks out of 100

The Marks Analysis option adds these marks and shows the total out of 200. It also shows the highest, lowest and average total.

## Attendance

The Attendance Check option asks for the attendance percentage of a subject.

If the attendance is 75% or above, the program shows that the attendance requirement is met and displays:

```text
Attendance marks: 5 / 5
```

If it is below 75%, the program shows that the full attendance marks are not applicable.

## Input Validation

The program checks the marks entered by the user.

Marks are accepted only within the correct range:

- CAT1: 0 to 50
- CAT2: 0 to 50
- TEE: 0 to 100

If the user enters an invalid value, the program shows an error message and asks for the input again.

The program also handles invalid menu choices and invalid attendance input.

## Python Concepts Used

The project uses basic Python concepts that I have used while learning Python:

- Variables and data types
- Input and output
- Strings
- Lists
- Dictionaries
- If-else statements
- Loops
- Functions
- Function parameters and return values
- Modules and imports
- Exception handling
- Basic calculations and searching

## Testing

I have used pytest for basic testing of the marks calculation.

To run the tests:

```bash
python -m pytest
```

The current tests check:

- Total marks calculation
- Total marks calculation when all marks are zero

## Data Storage

The project stores the subject information in memory while the program is running.

The data is not permanently saved. When the program is closed, the entered data is lost.

## Limitations

- The data is not saved after the program is closed.
- The project works through the terminal.
- There is no database or online storage.
- The project does not calculate an official VIT grade.
- The project is made for basic academic tracking.

## Objective

The main aim of this project is to make a simple program for managing subjects, marks and attendance while using the Python concepts learned in the course.