""" Weekly Task 2: bank.py

This program takes two amounts in cents, and calculates the total, then prints the result formatted as "€X.YY"."

References: https://docs.python.org/3/tutorial/inputoutput.html

"""

# Ask user to enter two amounts in cents
amount1 = int(input("Enter amount 1 in cents: "))
amount2 = int(input("Enter amount 2 in cents: "))

# Calculate total
total_cents = amount1 + amount2

# Convert to euros and cents
euros = total_cents // 100
cents = total_cents % 100

# Print formatted result
print(f"Total sum is €{euros}.{cents:02d}")
