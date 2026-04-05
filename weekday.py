""" Weekly Task 5: weekday.py

This program checks the current day of the week and prints whether it is a weekday or a weekend. It uses the datetime module to get the current day and determines if it is a weekday (Monday to Friday) or a weekend (Saturday and Sunday)."""

import datetime

# weekday() returns a number , Monday = 0 ... Sunday = 6
today = datetime.datetime.today().weekday()

# If number is less than 5, it is Monday-Friday (a weekday) else its a weekend
if today < 5:
    print("Today is a weekday")
else:
    print("Today is a weekend")