""" Weekly Task 2: bank.py

This program takes two amounts in cents, and calculates the total sum in euros and cents, then prints the result formatted as "€X.YY"."""

# Tells the user to enter two amounts in cents
amount1 = int(input("Enter amount1 in cents: "))
amount2 = int(input("Enter amount2 in cents: "))

# Add the amounts
total_cents = amount1 + amount2

# Convert to euros and cents
euros = total_cents // 100
cents = total_cents % 100

# Print formatted result
print(f"Total sum is €{euros}.{cents:02d}")
