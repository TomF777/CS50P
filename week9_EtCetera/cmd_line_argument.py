# Uses command-line argument

import sys

if len(sys.argv) == 1:
    print("hello")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("hello")
else:
    print("usage: cmd_line_argument.py [-n NUMBER]")
