"""
Outdated:

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
otherwise known as middle-endian order, which is arguably bad design.
Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
Dates in that format are also ambiguous.
Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that
prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
no matter the country, formatting years with four digits, months with two digits,
and days with two digits, “padding” each with leading zeroes as needed.


Implement a program that prompts the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the 'month_lst' below.

Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

"""

month_lst = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def create_iso_date(day, month, year):
    if day > 31: raise "Wrong day"
    if month > 12: raise "Wrong month"
    return f"{year}-{month:02}-{day:02}"


while True:
    user_date = input("Date: ")
    try:
        date_space = user_date.split()
        date_slash = user_date.split("/")


        if len(date_space) > 1:
            if "," not in date_space[1]: raise Exception
            day = int(date_space[1].strip(","))
            month = date_space[0]
            year = int(date_space[2])
            iso_date = create_iso_date(day, (month_lst.index(month) + 1), year)

        elif len(date_slash) > 1:
            day = int(date_slash[1])
            month = int(date_slash[0])
            year = int(date_slash[2])
            iso_date = create_iso_date(day, month, year)
        else:
            break
    except Exception as e:
        #print("exception: " + str(e))
        pass
    except ("Wrong day", "Wrong month"):
        #print("Wrong day or month")
        pass
    else:
        print(iso_date)
        break
