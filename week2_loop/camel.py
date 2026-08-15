"""
Implement a program that prompts the user for the name of a variable in camelCase
and outputs the corresponding name in snake_case.
Assume that the user’s input will indeed be in camel case.
"""

camel_case = input("camelCase:")

snake_case = ""

for character in camel_case:
    if character == character.upper():
        snake_case += "_" + character.lower()
    else:
        snake_case += character


print(snake_case)

