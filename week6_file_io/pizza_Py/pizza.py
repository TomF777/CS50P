"""
Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.

Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv, or if the specified file does not exist,
the program should instead exit via sys.exit.
"""

import sys
import csv
from tabulate import tabulate

# requires pip install tabulate


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith('.csv'):
    print("Not a CSV file")
    sys.exit(1)
else:
    try:
        file_name = sys.argv[1]
        item_lst = []

        with open(file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            header = reader.fieldnames

            for row in reader:
                item_lst.append([row[header[0]], row[header[1]], row[header[2]]])

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    else:
        print(tabulate(item_lst, header, tablefmt="grid"))

