"""
Implement a function that expects an IPv4 address as input as a str
and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Additionally implement, in a file called test_numb3rs.py, two or more functions
that collectively test your implementation of validate thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_numb3rs.py
"""


import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):
    match =  re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}$", ip)
    if match:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
