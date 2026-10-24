
from os import strerror


# Base exception class for student data errors.
class StudentsDataException(Exception):
    pass


# Custom exception for an invalid line in the file.
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__()
        self.line_number = line_number
        self.line_string = line_string


# Custom exception for an empty file.
class FileEmpty(StudentsDataException):
    pass


# Dictionary to store student names and total points.
data = {}

# Ask the user for the input filename.
file_name = input("Enter student's data filename: ")

try:
    # Open the file in text read mode.
    f = open(file_name, "rt")

    # Read all lines into a list.
    lines = f.readlines()
    f.close()

    # Check whether the file is empty.
    if len(lines) == 0:
        raise FileEmpty()

    # Process each line in the file.
    for i in range(len(lines)):

        # Get the current line.
        line = lines[i]

        # Split the line into columns.
        columns = line.split()

        # Each line must contain exactly three columns.
        if len(columns) != 3:
            raise WrongLine(i + 1, line)

        # Combine first name and last name.
        student = columns[0] + ' ' + columns[1]

        # Convert the points to a floating-point number.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)

        # Add points to the student's existing total.
        try:
            data[student] += points
        except KeyError:
            # Create a new dictionary entry if the student is not found.
            data[student] = points

    # Display students alphabetically with their total points.
    for student in sorted(data.keys()):
        print(student, '\t', data[student])

# Handle file input/output errors.
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Handle incorrectly formatted lines.
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) +
          " in source file: " + e.line_string)

# Handle an empty input file.
except FileEmpty:
    print("Source file empty")
