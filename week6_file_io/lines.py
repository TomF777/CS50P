"""
Implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.

If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .py, or if the specified file does not exist,
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
"""

import sys

code_lines = 0

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith('.py'):
    print("Not a Python file")
    sys.exit(1)
else:
    try:
        file_name = sys.argv[1]

        with open(file_name, "r") as file:
            for line in file:
                if not line.lstrip().startswith("#") and not len(line.lstrip())==0:
                    code_lines += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    print(code_lines)

