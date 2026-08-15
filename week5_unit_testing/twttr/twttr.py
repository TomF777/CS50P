"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr.
Implement a program that prompts the user for a str of text and
then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""


def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    output = ""

    for character in word:
        if character.upper() not in ['A', 'E', 'I', 'O', 'U']:
            output = output + character

    return f"{output}"


if __name__ == "__main__":
    main()
