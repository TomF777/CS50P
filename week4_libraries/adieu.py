"""
In a file called adieu.py, implement a program that prompts the user for names,
one per line, until the user inputs control-d.

Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and,
three names with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
"""

# requires pip install infelct
import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # catch CTRL+D from keyboard
        break

message = "\nAdieu, adieu, to " + p.join(names)
print(message)
