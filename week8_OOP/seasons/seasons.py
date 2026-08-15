"""
Implement a program that prompts the user for their date of birth in YYYY-MM-DD format
and then prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals, without any and between words.

Since a user might not know the time at which they were born, assume, for simplicity,
that the user was born at midnight (i.e., 00:00:00) on that date.

And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that it’s actually midnight,
on the same date. Use datetime.date.today to get today’s date.

------------------------------------------------------------------------------------------------
Requires:
pip install inflect

"""


from datetime import date
import sys
import inflect

def spell_age_in_minutes(birthday_date: date):
        current_date = date.today()
        diff_in_days = (current_date - birthday_date).days
        diff_in_minutes = diff_in_days * 24 * 60

        numbers = inflect.engine()
        result = numbers.number_to_words(diff_in_minutes, andword = '').capitalize(), \
                    numbers.plural_noun('minute', diff_in_minutes)

        return ' '.join(result)


def main():
    try:
        birthday_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit(1)
    else:
        res = spell_age_in_minutes(birthday_date)
        print(res)

if __name__ == "__main__":
    main()
