"""
Implement a function that expects a `str` of HTML as input, extracts any YouTube URL that's
the value of `src` attribute of an `iframe` element therein, and returns its shorter `youtu.be`
equivalent as `str`.
Expect that any such URL will be in one of the formats below:
 - http://youtube.com/embed/xvFZjo5PgG0
 - https://youtube.com/embed/xvFZjo5PgG0
 - https://www.youtube.com/embed/xvFZjo5PgG0

Assume that the value of src will be surrounded by double quotes.
Sssume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'^<iframe[ ]src="https?://(www\.)?youtube\.com/embed/(xvFZjo5PgG0)"', s)
    #print(match.group(2))
    if match:
        return "https://youtu.be/" + match.group(2)
    else:
        return None

if __name__ == "__main__":
    main()
