"""
Implement a program that:

- Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    - the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
- Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import sys
import csv


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    try:
        before_file = sys.argv[1]
        after_file = sys.argv[2]

        with open(before_file) as before, open(after_file, 'w') as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                writer.writerow({'first': first.strip(), 'last': last.strip(), 'house': house})

    except FileNotFoundError:
        print("Could not read", before_file)
        sys.exit(1)


