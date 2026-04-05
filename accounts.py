""" Weekly Task 3: accounts.py

This program takes a 10 digit account number as input, and prints the last four digits of the account number while hiding the other digits with "X". If the account number has less than or equal to 4 digits, it will print the account number as is without masking. """

# Asks to enter 10 digit number
account_number = input("Enter 10 digit account number: ")

# The last four digits of number inputted is shown, the other numbers are hidden with X
if len(account_number) <= 4:
    masked = account_number
else:
    masked = "X" * (len(account_number) -4) + account_number[-4:]

# Prints the number with all numbers hidden with X except the last 4 which would be seen.
print(masked)