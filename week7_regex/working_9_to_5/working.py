"""
Implement a function called convert that expects a `str` in any of the 12-hour
formats below and returns the corresponding `str` in 24-hour format (i.e., 9:00 to 17:00).

Expect that AM and PM will be capitalized (with no periods therein)
and that there will be a space before each.
Assume that these times are representative of actual times,
not necessarily 9:00 AM and 5:00 PM specifically.

- 9:00 AM to 5:00 PM
- AM to 5 PM
- 9:00 AM to 5 PM
- 9 AM to 5:00 PM

Raise a ValueError instead if the input to convert
is not in either of those formats or if either time
is invalid (e.g., 12:60 AM, 13:00 PM, etc.).

But do not assume that someone’s hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""

import re


def main():
    print(convert(input("Hours: ")))

def convert_to_24hour(hour, minute, am_pm):
    """
    convert AM/PM time to 24 hours format
    """
    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"


def convert(s):
    match = re.search(r"^(\d{1,2})(:(\d{2}))? (AM|PM) to (\d{1,2})(:(\d{2}))? (AM|PM)$", s)

    try:
        start_hour = int(match.group(1))
        start_min = int(match.group(3)) if match.group(3) else 0
        start_AM_PM = match.group(4)

        end_hour = int(match.group(5))
        end_min = int(match.group(7)) if match.group(7) else 0
        end_AM_PM = match.group(8)
    except:
        raise ValueError("Invalid time")

    if (start_hour > 12 or start_hour < 1) or \
        (end_hour > 12 or end_hour < 1) or \
        (start_min > 59 or start_min < 0) or \
        (end_min > 59 or end_min < 0):
        raise ValueError("Invalid time")

    start_time_24hour_format = convert_to_24hour(start_hour, start_min, start_AM_PM)
    end_time_24hour_format = convert_to_24hour(end_hour, end_min, end_AM_PM)

    return f"{start_time_24hour_format} to {end_time_24hour_format}"


if __name__ == "__main__":
    main()
