"""
Implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background)
on the input after resizing and cropping the input to be the same size,
saving the result as its output.

The program should instead exit via sys.exit:

- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.

"""

import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(('.jpg', '.jpeg', '.png')):
    print("Invalid input")
    sys.exit(1)
elif not sys.argv[2].endswith(('.jpg', '.jpeg', '.png')):
    print("Invalid input")
    sys.exit(1)
elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    print("Input and output have different extensions")
    sys.exit(1)
else:
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        with Image.open(input_file) as input_file, Image.open("shirt.png") as shirt:
            size = shirt.size
            resized_cropped = ImageOps.fit(input_file,
                                           size=size,
                                           method=Image.Resampling.BICUBIC,
                                           bleed=0.0,
                                           centering=(0.5, 0.5))
            resized_cropped.paste(shirt, shirt)
            resized_cropped.save(output_file)

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
