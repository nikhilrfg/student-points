# Python Student Points Calculator

## Project Overview

The Python Student Points Calculator reads student records from a text file, calculates the total points earned by each student, and displays the results in alphabetical order.

Each record contains a student's first name, last name, and points earned. If a student appears multiple times, the program adds their points together.

The program also handles missing files, empty files, invalid records, and incorrect point values using Python exception handling.

## Project Structure

```text
python-student-scores/
├── students_points.py
├── students.txt
├── repeated_students.txt
├── empty.txt
├── invalid_columns.txt
├── invalid_points.txt
├── sample_output.txt
└── README.md
```

The test files can be created manually in VS Code. The `missing.txt` file should not exist because it is used to test file-not-found handling.

## Features

- Reads student information from text files.
- Calculates total points for each student.
- Combines points from repeated student records.
- Stores student names and points in a dictionary.
- Sorts student names alphabetically.
- Uses custom exceptions for invalid lines and empty files.
- Handles missing or inaccessible files.
- Displays results in the terminal.

## Python Concepts Used

**File Handling:** Uses `open()`, `readlines()`, and `close()` to read student records.

**Dictionaries:** Stores student names as keys and accumulated points as values.

**Loops:** Processes each student record and displays the calculated totals.

**String Operations:** Uses `split()` to separate each line into three columns.

**Type Conversion:** Uses `float()` to convert points into numerical values.

**Exception Handling:** Uses `try`, `except`, and `raise` to detect and handle errors.

**Custom Exceptions:** Uses `StudentsDataException`, `WrongLine`, and `FileEmpty` for student-data validation.

## Requirements

- Python 3
- Visual Studio Code (recommended)
- Python extension for VS Code

No external Python libraries are required.

## How to Run

1. Open the `python-student-scores` folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run:

```powershell
python students_points.py
```

4. Enter the name of the student data file when prompted.

## Testing Scenarios

### Test 1: Valid Student Records

**Input file:** `students.txt`

File contents:

```text
John Smith 5
Anna Boleyn 4.5
John Smith 2
Anna Boleyn 11
Andrew Cox 1.5
```

Run:

```powershell
python students_points.py
```

Expected terminal output:

```text
Enter student's data filename: students.txt
Andrew Cox      1.5
Anna Boleyn     15.5
John Smith      7.0
```

Explanation:

- Andrew Cox = 1.5
- Anna Boleyn = 4.5 + 11 = 15.5
- John Smith = 5 + 2 = 7.0

The program combines repeated records and sorts students alphabetically.

### Test 2: Repeated Student Records

**Input file:** `repeated_students.txt`

File contents:

```text
John Smith 5
John Smith 10
John Smith 3
```

Expected terminal output:

```text
Enter student's data filename: repeated_students.txt
John Smith      18.0
```

Explanation:

The program calculates the total points for John Smith:

5 + 10 + 3 = 18.0

### Test 3: Missing Input File

**Input filename:** `missing.txt`

Expected terminal output:

```text
Enter student's data filename: missing.txt
I/O error occurred: No such file or directory
```

Explanation:

The program catches an `IOError` when the file cannot be opened and displays the operating system's error message.

### Test 4: Empty Input File

**Input file:** `empty.txt`

File contents: Empty file (0 bytes).

Expected terminal output:

```text
Enter student's data filename: empty.txt
Source file empty
```

Explanation:

The program raises the custom `FileEmpty` exception because the file contains no lines.

### Test 5: Incorrect Number of Columns

**Input file:** `invalid_columns.txt`

File contents:

```text
John Smith 5
Anna 10
```

Expected terminal output:

```text
Enter student's data filename: invalid_columns.txt
Wrong line #2 in source file: Anna 10
```

Explanation:

The second line contains only two columns instead of the required three columns:

1. First name
2. Last name
3. Points

The program raises the `WrongLine` exception.

### Test 6: Invalid Points Value

**Input file:** `invalid_points.txt`

File contents:

```text
John Smith 5
Anna Boleyn abc
```

Expected terminal output:

```text
Enter student's data filename: invalid_points.txt
Wrong line #2 in source file: Anna Boleyn abc
```

Explanation:

The value `abc` cannot be converted to a floating-point number using `float()`.

The program catches the conversion error and raises `WrongLine`.

## Testing Summary

| Test | Description | Expected Status |
|---|---|---|
| 1 | Valid student records | Pass |
| 2 | Repeated student records | Pass |
| 3 | Missing input file | Pass |
| 4 | Empty input file | Pass |
| 5 | Incorrect number of columns | Pass |
| 6 | Invalid points value | Pass |

**Note:** These are expected test results, not confirmed executions. Actual error messages and whitespace may vary depending on the operating system and file contents.

## Limitations

- Each record must contain exactly three whitespace-separated values.
- Student names must consist of one first name and one last name.
- Points must be valid numbers.
- Student names are case-sensitive.
- Results are displayed in the terminal and are not saved automatically.
- An empty file is rejected; a file containing only blank lines is treated as invalid data.

## Learning Outcomes

This project demonstrates how to use Python to read and process structured text files, accumulate numerical values using dictionaries, validate input data, implement custom exceptions, and display sorted results.

It provides practical experience with file handling and exception management in Python.