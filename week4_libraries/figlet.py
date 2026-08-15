"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art.
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

Implement a program that:

Expects zero or two command-line arguments:
 - Zero if the user would like to output text in a random font.
 - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
   and the second of the two should be the name of the font.

Prompts the user for a str of text.
Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font
or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
from pyfiglet import Figlet
import random


argv_len = len(sys.argv)
figlet = Figlet()
font_lst = figlet.getFonts()

if argv_len == 1:
# random font
    font_no = random.randrange(0, 570)
    font_name = font_lst[font_no]
elif argv_len == 3:
# specific font
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_lst:
        print("specific font")
        font_name = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = str(input("Input: "))

figlet.setFont(font=font_name)
print(figlet.renderText(user_input))
