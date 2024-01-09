import datetime
from datetime import date


def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        new_date_obj = date_obj.replace(year=date_obj.year + 4)
    return new_date_obj


def next_date(date_string):

    try:
        date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
        next_date_obj = add_year(date_obj)
        next_date_string = next_date_obj.strftime("%Y-%m-%d")
        print(f"date_obj : {date_obj}, next_date_obj: {next_date_obj}, "
              f"date string: {date_string}, converted string: {next_date_string}")
    except Exception as error:
        print(error)
    else:
        return next_date_string


today = date.today()  # Get today's date

print(next_date(str(today))) # Should return a year from today, unless today is Leap Day
