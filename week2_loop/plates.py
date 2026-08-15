"""
Requirements for a car plate are:

- All vanity plates must start with at least two letters.
- … vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate;
   they must come at the end.
   For example, AAA222 would be an acceptable … vanity plate;
   AAA22A would not be acceptable. The first number used cannot be a ‘0’.
- No periods, spaces, or punctuation marks are allowed.

Implement a program that prompts the user for a vanity plate and
then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.
is_valid returns True if 'plate_string' meets all requirements and False if it does not.
Assume that 'plate_string' will be a str.

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_string):

    cond_01 = 2 <= len(plate_string) <= 6
    cond_02 = plate_string[0:2].isalpha()
    cond_04 =  " " not in plate_string and "!" not in plate_string and "." not in plate_string

    first_digit = ""
    # find first digit
    for idx, char in enumerate(plate_string):
        if char.isdigit():
            first_digit = char
            first_digit_idx = idx
            break

    # number exists in plate
    if first_digit != "":
        number = plate_string[first_digit_idx:]
        cond_03 = number.isnumeric()
    else:
        cond_03 = True



    #print("first_digit: ", first_digit)
    return cond_01 and cond_02 and cond_04 and first_digit != "0" and cond_03



main()


