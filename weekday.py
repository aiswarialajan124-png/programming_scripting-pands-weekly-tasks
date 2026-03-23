import datetime

# weekday() returns a number , Monday = 0 ... Sunday = 6
today = datetime.datetime.today().weekday()

# If number is less than 5, it is Monday-Friday (a weekday) else its a weekend
if today < 5:
    print("Today is a weekday")
else:
    print("Today is a weekend")