# VIT GradeTrack - Project Design

## 1. Project Overview

VIT GradeTrack is a command-line Python project made to manage basic academic information of a student.

The program allows the user to add subjects, view subjects, enter marks, check attendance, analyze marks, search for a subject and delete a subject.

The project is divided into different Python modules so that each part of the program has a separate purpose.

## 2. Main Modules

### main.py
This is the main program file. It displays the menu and calls the required functions according to the user's choice.

### subject.py
This module manages subject-related operations such as adding, viewing, searching and deleting subjects. It also handles entering marks and checking attendance.

### calculator.py
This module performs total marks calculation and basic marks analysis.

### validator.py
This module checks whether the marks entered by the user are valid.

### tests/test_calculator.py
This file contains basic tests for the marks calculation function.

## 3. Functional Requirements

The system should provide the following functions:

1. The user can add a new subject with its name and subject code.
2. The user can view all added subjects.
3. The user can enter CAT1, CAT2 and TEE marks for a subject.
4. The user can check the attendance percentage of a subject.
5. The user can calculate and view total marks.
6. The user can view basic marks analysis such as highest, lowest and average total.
7. The user can search for a subject using its subject code.
8. The user can delete a subject from the list.
9. The program should show an appropriate message when the user enters an invalid menu option.
10. The program should handle invalid numerical input for marks.

## 4. Non-Functional Requirements

1. **Usability:** The program should have a simple menu so that a beginner can understand and use it.

2. **Reliability:** The program should handle invalid marks and invalid menu choices without stopping unexpectedly.

3. **Maintainability:** The program is divided into separate Python modules so that individual parts can be understood and modified easily.

4. **Performance:** The program should perform subject searches and marks calculations quickly for a normal number of subjects.

5. **Readability:** The code should use meaningful variable and function names and a simple structure.

## 5. Project Architecture

The project is divided into different Python files. Each file has a specific purpose.

```text
              USER
                |
                v
             main.py
          (Main Menu)
                |
       ---------------------
       |         |         |
       v         v         v
   subject.py  calculator.py  validator.py
       |           |
       |           |
       v           v
  Subject Data   Marks Analysis

## 6. Basic Program Workflow

```text
Start
  |
  v
Display Menu
  |
  v
Take User Choice
  |
  +---- Add Subject ------> Add subject details
  |
  +---- View Subjects ----> Display subjects
  |
  +---- Enter Marks ------> Enter CAT1, CAT2 and TEE
  |
  +---- Attendance -------> Check attendance
  |
  +---- Analysis ---------> Calculate totals and analysis
  |
  +---- Search -----------> Search subject by code
  |
  +---- Delete -----------> Delete subject
  |
  +---- Exit -------------> End Program
  |
  v
Return to Menu 

## 7. Data Structures Used

The project uses basic Python data structures to store and process information.

### List

A list is used to store all the subjects added by the user.

Example:

subjects = []

Each subject is added to this list.

### Dictionary

A dictionary is used to store the details of each subject.

Example:

subject = {
    "name": "Problem Solving and Programming",
    "code": "CSE1021"
}

When marks are entered, CAT1, CAT2 and TEE marks are also stored in the dictionary.

### Strings

Strings are used for subject names, subject codes and user input.

### Integer and Float

Integers are used for marks, while a float is used for attendance percentage.

## 8. Python Concepts Used

The project uses the following Python concepts:

1. Variables and data types
2. Input and output
3. Conditional statements
4. Loops
5. Lists
6. Dictionaries
7. Strings
8. Functions
9. Function parameters and return values
10. Modules and imports
11. Exception handling
12. Basic searching and calculations

These concepts are used in different parts of the project to manage subjects, marks and attendance.

## 9. Testing

Basic testing was performed to check whether the marks calculation functions correctly.

The project uses pytest for testing.

The tests check:

1. Correct calculation of total marks.
2. Correct calculation when all marks are zero.

The tests can be run using:

```bash
python -m pytest

## 10. Limitations

1. The data is stored only while the program is running.
2. The data is lost when the program is closed.
3. The project does not use a graphical user interface.
4. The project does not calculate an official VIT grade because official grade conversion rules are not defined in the project requirements.
5. The project is designed for basic academic tracking and does not include advanced features such as login or online data storage.