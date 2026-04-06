""" Weekly Task 3: accounts.py

This program takes a 10-digit account number as input and hides all but the last four digits using 'X'. If the account number is less than or equal to 4 digits, it will display the number as is without masking.

References: https://docs.python.org/3/tutorial/controlflow.html"""

# Asks to enter accountnumber
account_number = input("Enter account number: ")

# The last four digits of number inputted is shown, the other numbers are hidden with X
if len(account_number) <= 4:
    masked = account_number
else:
    masked = "X" * (len(account_number) - 4) + account_number[-4:]

# Prints the number with all numbers hidden with X except the last 4 which would be seen.
print(masked)