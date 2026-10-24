# Student Points Calculator

## Project Overview

This Python program reads student records from a text file, calculates the total points earned by each student, and displays the results in alphabetical order.

The program demonstrates file handling, dictionaries, loops, exception handling, and custom exception classes.

**Original exercise source:** Cisco Networking Academy (NetAcad), Python Essentials 2.

## Project Structure

```text
python-student-scores/
├── students_points.py
├── students.txt
├── README.md
└── sample_output.txt
```

## Features

- Reads student records from a text file.
- Processes student first names, last names, and points.
- Combines multiple records belonging to the same student.
- Uses a dictionary to store total points.
- Sorts students alphabetically.
- Handles missing files and invalid student records.
- Uses custom exceptions for incorrect lines and empty files.

## Python Concepts Used

### 1. Custom Exceptions

```python
class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__()
        self.line_number = line_number
        self.line_string = line_string

class FileEmpty(StudentsDataException):
    pass
```

These classes handle errors specific to student data.

### 2. File Handling

```python
f = open(file_name, "rt")
lines = f.readlines()
f.close()
```

Opens the input file, reads its contents into a list, and closes the file.

### 3. Splitting Student Records

```python
columns = line.split()
```

Separates each line into three values: first name, last name, and points.

### 4. Dictionary Operations

```python
try:
    data[student] += points
except KeyError:
    data[student] = points
```

Adds points to an existing student or creates a new dictionary entry.

### 5. Sorting Results

```python
for student in sorted(data.keys()):
    print(student, '\t', data[student])
```

Displays student names alphabetically with their total points.

## How to Run

1. Open the project folder in Visual Studio Code.
2. Create a file named `students.txt`.
3. Open the PowerShell terminal.
4. Run:

```powershell
python students_points.py
```

5. Enter the input filename when prompted.

## Sample Input

Contents of `students.txt`:

```text
John Smith 5
Anna Boleyn 4.5
John Smith 2
Anna Boleyn 11
Andrew Cox 1.5
```

## Expected Output

```text
Enter student's data filename: students.txt
Andrew Cox      1.5
Anna Boleyn     15.5
John Smith      7.0
```

## Testing Scenarios

| Test | Description | Expected Result |
|---|---|---|
| 1 | Valid student records | Displays total points |
| 2 | Student appears multiple times | Adds points together |
| 3 | Missing input file | Displays an I/O error |
| 4 | Empty input file | Displays `Source file empty` |
| 5 | Incorrect number of columns | Displays a wrong-line error |
| 6 | Invalid points value | Displays a wrong-line error |

## Requirements

- Python 3
- Visual Studio Code (recommended)
- Python extension for VS Code

No third-party Python packages are required.

## Limitations

- Each nonempty input line must contain exactly three whitespace-separated values.
- Student names must consist of one first name and one last name.
- Points must be convertible to floating-point numbers.
- Student names are case-sensitive.
- The program displays results in the terminal rather than saving them to a separate file.

## Acknowledgment

This project is based on a student-points exercise from Cisco Networking Academy's Python Essentials 2 course. Comments and minor code improvements have been added for educational practice.