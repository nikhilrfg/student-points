
from os import strerror

# Base exception for student data errors
class StudentsDataException(Exception):
    pass


# Exception for an incorrect line in the file
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__()
        self.line_number = line_number
        self.line_string = line_string


# Exception for an empty file
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__()


# Dictionary to store student names and total points
data = {}

# Ask the user for the filename
file_name = input("Enter student's data filename: ")

try:
    # Open and read all lines from the file
    with open(file_name, "rt") as f:
        lines = f.readlines()

    # Check whether the file is empty
    if len(lines) == 0:
        raise FileEmpty()

    # Process each line
    for i in range(len(lines)):

        line = lines[i]

        # Split the line into separate elements
        columns = line.split()

        # Every line must contain exactly 3 elements
        if len(columns) != 3:
            raise WrongLine(i + 1, line)

        # Combine first name and last name
        student = columns[0] + ' ' + columns[1]

        # Convert points into a floating-point number
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)

        # Add points if the student already exists
        try:
            data[student] += points
        except KeyError:
            # Otherwise, create a new dictionary entry
            data[student] = points

    # Print the students in alphabetical order
    for student in sorted(data.keys()):
        print(student, '\t', data[student])

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

except WrongLine as e:
    print("Wrong line #" + str(e.line_number) +
          " in source file: " + e.line_string)

except FileEmpty:
    print("Source file empty")
