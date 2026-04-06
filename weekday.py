""" Weekly Task 5: weekday.py

This program checks the current day of the week and prints whether it is a weekday or a weekend.

References: https://docs.python.org/3/library/datetime.html"""

import datetime

# Get current day (Monday = 0 ,Sunday = 6)
today = datetime.datetime.today().weekday()

# Check if weekday or weekend 
if today < 5:
    print("Today is a weekday")
else:
    print("Today is a weekend")