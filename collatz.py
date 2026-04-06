""" Weekly Task 4: collatz.py

This program generates the Collatz sequence for a given positive integer and continues until it reaches 1.

References: https://oeis.org/A006577 """

# Ask user to enter a positive integer
num = int(input("Enter a positive integer: "))

# Generate Collatz sequence
while num != 1:
    print(num, end=" ")

    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

# Print final 1
print(1)