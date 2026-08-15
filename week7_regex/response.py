"""
Using either `validator-collection` or `validators` from PyPI,
implement a program that prompts the user for an email address
 via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address.

 You may not use `re`. And do not validate whether the email address’s domain name actually exists.

Note that you can install validator-collection with:
`pip install validator-collection`

Note that you can install validators with:
`pip install validators`
"""


import validators


def main():
    print(check_email(input("What's your email address? ")))

def check_email(email):
    result = validators.email(email)
    if result:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
